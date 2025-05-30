# GMail - A Case Study

Ok, now that we have the understanding of primitive and composite types, let's take a real world example and see how the concepts we have studied so far map to them.

In any mail application, you see a bunch of mails, put together in various mailboxes. A mail has several properties like the sender's id, the receiver's id, the time sent, the subject and body of the mail among other things. The mailbox has a name like 'Inbox', 'Sent mail' etc and contains a collection of mails. How do we represent these mails?

A mail can be represented using a map structure. We have several properties like from, to, subject, body etc as keys and their corresponding values being the actual values:

`{'from': 'joe@example.com', 'to': 'doe@example.net', 'subject': 'Meeting on Friday', 'body': 'Are you attending the meeting on Friday?' }`

A mailbox contains a list of mails:

`'inbox': [ { ... mail1 ... }, { ... mail2 ... } ... ]`