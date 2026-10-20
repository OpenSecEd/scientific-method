---
name: Reflection on Science in Security
regex: ^389772$
due_at: '2026-12-06T19:00:00Z'
points_possible: 1.0
published: true
modules:
- module: ^Scientificity,\ part\ 2\ \(week\ 49\)$
  position: 9
---
## Introduction

Let's think a bit about how we know what we teach in the security
courses are good things or not. This will let us combine all the classes
of methods that we've covered during the course. Remember also what they
wrote in [SoK: Science, Security and the Elusive Goal of Security as a
Scientific
Pursuit]($CANVAS_COURSE_REFERENCE$/assignments/SoK%3A%20Science%2C%20Security%20and%20the%20Elusive%20Goal%20of%20Security%20as%20a%20Scientific%20Pursuit "SoK: Science, Security and the Elusive Goal of Security as a Scientific Pursuit"){course-type="assignments"
published="true"
api-endpoint="$CANVAS_COURSE_REFERENCE$/assignments/SoK%3A%20Science%2C%20Security%20and%20the%20Elusive%20Goal%20of%20Security%20as%20a%20Scientific%20Pursuit"
api-returntype="Assignment"}: we wouldn't want to just make tautological
restatements of our assumptions.

## Assignment

Before the seminar, pick THREE (3) of the topics below. For each one you
picked, outline a methodology for how to evaluate it. **The focus is on
how do you know that it is correct**: reflect on what you\'ve learned in
this course (and TAMOS) and apply it to these topics that you\'re
typically taught in the other security courses. **Sure these all make
sense, but really, how can we know for sure that this is actually good
advice?**

### Passwords

To do password-based authentication, we're taught that we should salt
and hash the passwords. The user submits the password to the server, the
server adds a 128-bit salt (random number) and hashes the password using
SHA256, then hashes the hash, and hashes that hash, and so on for 1000
times. That final hash is used to check if it's the same as the one
stored. If so, the user is accepted.

### Programming in not-C

When we write programs, we should avoid languages like C or C++. (This
is even suggested by some US government agencies.) It's better to use a
language like Rust, which has built-in memory safety. Writing programs
in Rust will result in fewer security vulnerabilities in the programs
and will thus be more secure.

### Mandatory Access Control (MAC)

The implementation of Mandatory Access Control (MAC) mechanisms, such as
the Bell-LaPadula Model, is crucial in environments that demand high
levels of security and confidentiality. Organizations that handle
sensitive or classified information (e.g. military, government agencies)
must ensure that data access is strictly regulated. MAC models achieve
this by enforcing control policies that limit access based on user
clearance levels.

### Multi-Factor Authentication (MFA)

Multi-Factor Authentication (MFA) is an effective way to enhance
security. By requiring users to provide two or more verification factors
before granting access, MFA adds an additional layer of protection
beyond just the password. The methods of implementing MFA varies; such
as SMS, email, or authenticator apps.

### Firewalls

Firewalls are a fundamental component of network security that are
taught in introductory courses. They act as barriers between trusted and
untrusted networks by controlling incoming and outgoing network traffic
based on predetermined security rules. Firewalls are necessary to
prevent unauthorized access and attacks.

### Social Engineering Awareness Training

Security courses often emphasize the importance of educating employees
about social engineering attacks. The training aims to help employees
recognize and avoid common tactics used in attacks, such as phishing.

### Encrypt Data-at-Rest

One common security practice is encrypting data-at-rest to protect
sensitive information stored on devices or servers. By encrypting the
data, unauthorized users are prevented from accessing it without the
appropriate decryption key.

### Regular Security Updates

It is standard advice to regularly update software to stay protected
against newly discovered vulnerabilities. Updates often include patches
for security flaws that could be exploited by attackers.

### Penetration Testing (Pentesting)

Penetration testing, commonly referred to as pentesting, is a proactive
approach to evaluating the security of a computer system, network, or
application by simulating an attack from malicious outsiders and
insiders. Pentesting can help identify vulnerabilities before attackers
exploit them. A comprehensive pentest involves several stages,
including\
planning, reconnaissance, scanning, exploitation, and reporting. After a
successful pentest the system will be secure.

### Adding features

The Bank has used the same back-end software for 50 years (written in
COBOL). This software works and manages the Bank's accounts. Previously
the Bank's staff interacted with the software, e.g. to transfer money
between accounts.

The Bank hired FutureSoftware to add a web-based front-end so that the
customers can interact with the software directly. That way customers
can transfer money between accounts without the need for Bank staff to
do it for them. (They wrote the software in Rust.) FutureSoftware says
that this is secure.

The Bank then asked VETCYB consultants to evaluate if this is secure.
How would go do it?

