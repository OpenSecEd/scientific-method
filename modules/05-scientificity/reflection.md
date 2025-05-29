# Introduction

Let's think a bit about how we know what we teach in the security courses are
good things or not. This will let us combine all the classes of methods that 
we've covered during the course. Remember also what they wrote in Security as a 
Scientific Pursuit: we wouldn't want to just make tautological restatements of 
our assumptions.

Before the seminar, pick THREE (3) of the topics below. For each one you 
picked, outline a methodology for how to evaluate it.

## Passwords

To do password-based authentication, we're taught that we should salt
and hash the passwords. The user submits the password to the server,
the server adds a 128-bit salt (random number) and hashes the password
using SHA256, then hashes the hash, and hashes that hash, and so on for 1000 
times. That final hash is used to check if it's the same as the one stored. If 
so, the user is accepted. Is this password-based authentication scheme secure?

## Programming in not-C

When we write programs, we should avoid languages like C or C++. (This is even 
suggested by some US government agencies.) It's better to use a language like 
Rust, which has built-in memory safety. Writing programs in Rust will result in 
fewer security vulnerabilities in the programs and will thus be more secure. Is 
this really true?

## Adding features

The Bank has used the same back-end software for 50 years (written in COBOL). 
This software works and manages the Bank's accounts. Previously the Bank's 
staff interacted with the software, e.g. to tranfer money between accounts.

The Bank hired FutureSoftware to add a web-based front-end so that the 
customers can interact with the software directly. That way customers can 
transfer money between accounts without the need for Bank staff to do it for 
them. (They wrote the software in Python.)

The Bank then asked VETCYB consultants to evaluate if this is secure. How would 
go do it?

## Mandatory Access Control (MAC)

The implementation of Mandatory Access Control (MAC) mechanisms, such
as the Bell-LaPadula Model, is considered crucial in environments that
demand high levels of security and confidentiality. Organizations that
handle sensitive or classified information must ensure that data access
is strictly regulated. MAC models achieve this by enforcing control
policies that limit access based on user clearance levels. Does this work?

## Multi-Factor Authentication (MFA)

Multi-Factor Authentication (MFA) is promoted as an effective way to enhance 
security. By requiring users to provide two or more verification factors before 
granting access, MFA adds an additional layer of protection beyond just the 
password. The methods of implementing MFA varies; such as SMS, email, or 
authenticator apps. Is this secure?

## Firewalls

Firewalls are a fundamental component of network security that are
taught in introductory courses. They act as barriers between trusted and
untrusted networks by controlling incoming and outgoing network traffic
based on predetermined security rules. Firewalls can prevent
unauthorized access and attacks. Is this true?

## Social Engineering Awareness Training

Security courses often emphasize the importance of educating employees
about social engineering attacks. The training aims to help employees
recognize and avoid common tactics used in attacks, such as phishing.
Is this secure? How effective, if at all, is such training in practice at 
preventing social engineering breaches over time?

## Encrypt Data-at-Rest

One common security practice is encrypting data-at-rest to protect
sensitive information stored on devices or servers. By encrypting the
data, unauthorized users are prevented from accessing it without the
appropriate decryption key. Is this secure?

## Regular Security Updates

It is standard advice to regularly update software to stay protected
against newly discovered vulnerabilities. Updates often include patches
for security flaws that could be exploited by attackers. Does this contribute 
to increased security?

## Penetration Testing (Pentesting)

Penetration testing, commonly referred to as pentesting, is a proactive
approach to evaluating the security of a computer system, network,
or application by simulating an attack from malicious outsiders and
insiders. Pentesting can help identify vulnerabilities before attackers
exploit them. A comprehensive pentest involves several stages, including
planning, reconnaissance, scanning, exploitation, and reporting. After a 
successful pentest the system will be secure. Is this true?
