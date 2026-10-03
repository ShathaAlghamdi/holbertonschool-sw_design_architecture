#!/usr/bin/env python3
"""Observer pattern example with a topic-aware subscriber."""


class NewsSubject:
    """Publish news events to subscribed observers."""

    def __init__(self):
        self._observers = []

    def subscribe(self, observer, topics=None):
        """Subscribe an observer to selected topics or all topics."""
        self._observers.append((observer, topics))

    def unsubscribe(self, observer):
        """Remove an observer from the subscriber list."""
        self._observers = [
            (current, topics)
            for current, topics in self._observers
            if current is not observer
        ]

    def notify(self, topic, data):
        """Notify matching observers using a safe snapshot."""
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Log selected news topics."""

    def update(self, topic, data):
        """Print a log notification."""
        print(f"log:{topic}={data}")


class EmailObserver:
    """Receive all news topics by email."""

    def update(self, topic, data):
        """Print an email notification."""
        print(f"email:{topic}={data}")


class SmsObserver:
    """Receive selected news topics by SMS."""

    def update(self, topic, data):
        """Print an SMS notification."""
        print(f"sms:{topic}={data}")


def main():
    """Run the Observer example."""
    subject = NewsSubject()

    log_observer = LogObserver()
    email_observer = EmailObserver()
    sms_observer = SmsObserver()

    subject.subscribe(log_observer, topics={"sports", "breaking"})
    subject.subscribe(email_observer)
    subject.subscribe(sms_observer, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
