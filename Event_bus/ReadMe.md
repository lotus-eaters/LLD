# Event-Driven Architecture: Building an Event Bus

Imagine you are building an e-commerce platform.

Whenever an order is placed, several services may need to know about it:

- Email Service sends an order confirmation.
- Inventory Service updates stock.
- Analytics Service records the purchase.
- Notification Service sends a notification.
- Delivery Service updates delivery information.

## The Problem

Should the `Order Service` directly know about all five services?

```text
Order Service
      |
      |---> Email Service
      |---> Inventory Service
      |---> Analytics Service
      |---> Notification Service
      |---> Delivery Service
```

This creates tight coupling between services. The `Order Service` becomes responsible for knowing:

- Which services need order information.
- How to communicate with each service.
- What happens when one of the services fails.
- How to execute these operations asynchronously.

## The Solution: Event Bus

Instead of communicating directly with every service, the `Order Service` publishes an event.

An intermediate component called an **Event Bus** receives the event and distributes it to all interested listeners.

```text
Order Service
      |
      | publishes OrderPlacedEvent
      v
  Event Bus
      |
      |---> Email Listener
      |---> Inventory Listener
      |---> Analytics Listener
      |---> Notification Listener
      |---> Delivery Listener
```

The Event Bus keeps services decoupled. The `Order Service` only needs to know how to publish an event; it does not need to know who receives it.

## Event Bus Requirements

An Event Bus should support:

- Subscribing to events.
- Unsubscribing from events.
- Publishing events.
- Multiple listeners for the same event.
- Asynchronous event execution.
- Failure isolation between listeners.
- Type-safe event handling.
- Graceful shutdown.

# What Is an Event?

An event represents something that has already happened in the system.

Examples include:

```text
OrderPlaced
PaymentSuccessful
UserRegistered
```

Different events may contain different data. Therefore, we can define a common event interface.

```java
public interface Event {
}
```

An event can then implement this interface:

```java
public class OrderPlacedEvent implements Event {
    private final String orderId;
    private final String customerName;
    private final Date createdAt;
    private final double amount;

    public OrderPlacedEvent(
            String orderId,
            String customerName,
            Date createdAt,
            double amount
    ) {
        this.orderId = orderId;
        this.customerName = customerName;
        this.createdAt = createdAt;
        this.amount = amount;
    }

    public String getOrderId() {
        return orderId;
    }

    public String getCustomerName() {
        return customerName;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public double getAmount() {
        return amount;
    }
}
```

Other events can have their own structure:

```java
public class PaymentSuccessfulEvent implements Event {
    private final String paymentId;
    private final String orderId;
    private final double amount;

    public PaymentSuccessfulEvent(
            String paymentId,
            String orderId,
            double amount
    ) {
        this.paymentId = paymentId;
        this.orderId = orderId;
        this.amount = amount;
    }

    public String getPaymentId() {
        return paymentId;
    }

    public String getOrderId() {
        return orderId;
    }

    public double getAmount() {
        return amount;
    }
}
```

# Who Receives an Event?

The components that receive events are commonly called:

- Listeners.
- Subscribers.
- Event handlers.
- Consumers.

A listener subscribes to one or more specific event types.

For example:

- An email listener may listen only to `OrderPlacedEvent`.
- A wallet listener may listen only to `PaymentSuccessfulEvent`.
- An analytics listener may listen to multiple event types.

## Generic Event Listener

Generics allow us to create type-safe listeners:

```java
public interface EventListener<T extends Event> {
    void onEvent(T event);
}
```

The type parameter `T` must extend the base `Event` interface.

## Email Listener

```java
public class EmailListener
        implements EventListener<OrderPlacedEvent> {

    private final MailChimpInstance mailChimpInstance =
            MailChimpInstanceGenerator.getInstance();

    @Override
    public void onEvent(OrderPlacedEvent event) {
        mailChimpInstance.sendEmail(
                event,
                "order-confirmation-template"
        );
    }
}
```

The `EmailListener` receives only `OrderPlacedEvent` objects.

## Inventory Listener

```java
public class InventoryListener
        implements EventListener<OrderPlacedEvent> {

    @Override
    public void onEvent(OrderPlacedEvent event) {
        // Update inventory using the order information
    }
}
```

## Wallet Listener

```java
public class WalletListener
        implements EventListener<PaymentSuccessfulEvent> {

    @Override
    public void onEvent(PaymentSuccessfulEvent event) {
        // Update wallet or payment-related information
    }
}
```

# Registering Listeners

All listeners must be registered somewhere.

The Event Bus maintains information about:

- Which event types exist.
- Which listeners are subscribed to each event type.
- Which listeners should receive a published event.

```text
OrderPlacedEvent
      |
      |---> EmailListener
      |---> InventoryListener
      |---> AnalyticsListener

PaymentSuccessfulEvent
      |
      |---> WalletListener
      |---> EmailListener
```

# Event Bus Interface

```java
public interface EventBus {

    <T extends Event> void subscribe(
            Class<T> eventType,
            EventListener<T> listener
    );

    <T extends Event> void unsubscribe(
            Class<T> eventType,
            EventListener<T> listener
    );

    void publish(Event event);

    void shutdown();
}
```

## Main Operations

### Subscribe

Registers a listener for a specific event type.

```java
eventBus.subscribe(OrderPlacedEvent.class, emailListener);
```

### Unsubscribe

Removes a listener from a specific event type.

```java
eventBus.unsubscribe(OrderPlacedEvent.class, emailListener);
```

### Publish

Publishes an event to the Event Bus.

```java
eventBus.publish(orderPlacedEvent);
```

The Event Bus finds all listeners registered for the event's class and sends the event to them.

### Shutdown

Stops the executor and releases resources.

```java
eventBus.shutdown();
```

# Asynchronous Event Bus

An asynchronous Event Bus can use an `ExecutorService` to execute listeners without blocking the publisher.

```java
public class AsyncEventBus implements EventBus {

    private final Map<
            Class<? extends Event>,
            List<EventListener<? extends Event>>
    > listeners = new ConcurrentHashMap<>();

    private final ExecutorService executor =
            Executors.newFixedThreadPool(4);

    @Override
    public <T extends Event> void subscribe(
            Class<T> eventType,
            EventListener<T> listener
    ) {
        listeners
                .computeIfAbsent(
                        eventType,
                        key -> new CopyOnWriteArrayList<>()
                )
                .add(listener);
    }

    @Override
    public <T extends Event> void unsubscribe(
            Class<T> eventType,
            EventListener<T> listener
    ) {
        List<EventListener<? extends Event>> eventListeners =
                listeners.get(eventType);

        if (eventListeners != null) {
            eventListeners.remove(listener);
        }
    }

    @Override
    public void publish(Event event) {
        List<EventListener<? extends Event>> eventListeners =
                listeners.get(event.getClass());

        if (eventListeners == null) {
            return;
        }

        for (EventListener<? extends Event> listener : eventListeners) {
            executor.submit(() -> dispatch(listener, event));
        }
    }

    private <T extends Event> void dispatch(
            EventListener<T> listener,
            Event event
    ) {
        try {
            listener.onEvent((T) event);
        } catch (Exception exception) {
            // Log the exception so that one listener
            // does not affect the others
            exception.printStackTrace();
        }
    }

    @Override
    public void shutdown() {
        executor.shutdown();
    }
}
```

> In production code, the unchecked cast in `dispatch` should be handled carefully. A more advanced implementation can use a wrapper or a type-safe internal registration model to avoid the cast.

# Example Usage

```java
EventBus eventBus = new AsyncEventBus();

EmailListener emailListener = new EmailListener();
InventoryListener inventoryListener = new InventoryListener();

eventBus.subscribe(OrderPlacedEvent.class, emailListener);
eventBus.subscribe(OrderPlacedEvent.class, inventoryListener);

OrderPlacedEvent event = new OrderPlacedEvent(
        "ORD-101",
        "Alice",
        new Date(),
        1499.99
);

eventBus.publish(event);
```

The `Order Service` only publishes the event:

```java
eventBus.publish(orderPlacedEvent);
```

It does not need to know that the email and inventory listeners are subscribed.

# Key Benefits

- **Loose coupling:** Publishers do not depend directly on consumers.
- **Extensibility:** New listeners can be added without modifying the publisher.
- **Asynchronous execution:** Listeners can run in background threads.
- **Failure isolation:** A failure in one listener does not necessarily stop the others.
- **Multiple subscribers:** Many listeners can react to the same event.
- **Improved maintainability:** Each listener handles one specific responsibility.
