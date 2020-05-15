##############################
Writing a great commit message
##############################

An often overlooked part of Git is the commit message. The usefulness of many
of Git's features rely on well structured commit messages.

A commit message structure:

.. code-block:: none

    Subject line in 50 chars or less

    Following a blank line after the subject line is the commit message
    body, containing a more detailed explaination of the change.
    This should be word-wrapped at 72 characters.

    The body can consist of as many lines as necessary to fully
    explain in detail why the change is necessary. You should
    explain the problem that this commit is solving and focus on
    why this change is necessary rather than explaining the "how"
    (the reviewer can review the code for that detail).

    Include any side effects and consequences of the change.

    Many CLI based tools such as `git log`, `git shortlog`,
    `git rebase`, are significantly more useful when the commit
    messages follow these best practices.

    Finally the last "block" (a section without further blank lines
    following it) is for metadata such as sign-offs, references, and
    issue numbers.

    Issue: #123
    See-also: #456
    Ref: https://example.com/relevant-article-or-link
    Co-authored-by: Firstname Lastname <email>
    Signed-off-by: Firstname Lastname <email>


We will break down the major sections below.


The subject line
================

The subject line should be short and sweet, providing enough detail for the
reader to immediately have a decent idea about what the commit is about.

From the ``git commit`` manpage:

    Though not required, it’s a good idea to begin the commit message with a
    single short (less than 50 character) line summarizing the change,
    followed by a blank line and then a more thorough description. The text up
    to the first blank line in a commit message is treated as the commit
    title, and that title is used throughout Git. For example,
    Git-format-patch(1) turns a commit into email, and it uses the title on
    the Subject line and the rest of the commit in the body.

**Best practices:**

* Keep the subject line short (50 characters)
* The first letter of the subject line should be capitalized
* The subject line should not end with any punctuation
* The subject line should be written in imperative mood
* Immediately following subject line is a blank line
* Descriptive enough that one can get the gist of the change

**Good examples:**

.. raw:: html

    <ul>
      <li><p class="text-success">Allow pyyaml >= 5</p></li>
      <li><p class="text-success">Bump version to 2.0.0-SNAPSHOT</p></li>
      <li><p class="text-success">Fix double inderection of name templates</p></li>
      <li><p class="text-success">Add Private and WIP change support for Gerrit</p></li>
    </ul>

**Bad examples:**

.. raw:: html

    <ul>
      <li><p class="text-danger">Fix build issue</p></li>
      <li><p class="text-danger">Fixes delete-all command when no option is provided.</p></li>
      <li><p class="text-danger">Adding view for the Delivery Pipeline Plugin</p></li>
      <li><p class="text-danger">test non-default value of attach-build-log</p></li>
    </ul>


The commit body
===============

Following a blank line after the subject line, the commit body is where you
can explain your change in full details.

**Best practices:**

* Keep lines under 72 characters
* Explain what and why instead of how

Git as well many tools that parse Git commits do not automatically wrap text
so you must manually do this yourself. Keeping the limit to 72 characters is
good practice to allow for Git to do indentation and still be under 80
characters total.

Put yourself in the shoes of the reviewer of the change. If someone proposed
this change to you, what information would you like to know about it before
you will approve the change?

Reviewers can look at the diff to see what exactly was changed so focus on
telling the reviewer why they should accept your change. You are essentially
writing a project proposal here so provide as much detail as possible.

If you are fixing code or a test, include details on how to reproduce the
problem so that the reviewer doesn't have to reach out to you for further
details on how to retest.

**Good example A:**

.. code-block:: none

    Fix the yaml load warning

    In the new version of PyYAML the API changed to be more explicit. Now
    the default value for the Loader is None, see:

    https://github.com/yaml/pyyaml/blob/5.1/lib3/yaml/__init__.py#L103

    The load is unsafe. It's better to use safe_load function.

    Change-Id: Ia1cd16f2ff970ca220a266c99b6554dd4254ebd9

**Good example B:**

.. code-block:: none

    Add 'secret-token' parameter to gitlab trigger

    This adds support for the job specific secret token in the
    gitlab build trigger.

    This feature was added to the "Gitlab Plugin" with version 1.4.1
    (released Sep 24, 2016).
    Excerpt from the changelog:
     "Add possiblity to configure secret tokens per job to allow
     only web hooks with the correct token to trigger builds."

    Change-Id: Id1ede4a6a51a231f60a39bfaefbadd8f849076e4


Commit message trailer
======================

The final block of a commit message is for trailers. Similar to email it is
where you sign off on your message as well as include other useful metadata.
Typically for references to issues or links to pages for additional
information.

**Best Practices:**

* Use the form ``Key: Value`` when entering trailers
* Make sure the last block has no blank lines in between entries
* If there is a relevant issue, refer to it here
* Give credit via ``Co-authored-by`` to other folks who worked on this commit

**Example:**

.. code-block:: none

    Issue: ABC-123
    Ref: https://example.com/blog-about-issue
    Change-Id: Iaa40ef0377409e08e6efd41aa967249f9d3c4xyz
    Co-authored-by: Bob <bob@example.com>
    Signed-off-by: Tim <tim@example.com>

**Signed-off-by**

In some open source projects folks leave a
``Signed-off-by: Firstname Lastname <someone@example.com>``.

This can be added automatically via the ``git commit -s`` command, it's a
convenience parameter but you can also type it in by hand when writing your
commit message.

Signed-off-by doesn't really mean much in most projects but some open source
projects use it as a way of indicating that you have signed off on an
official document such as a **Contributor License Agreement (CLA)** or a
**Developer Certificate of Origin**.

Reference: https://developercertificate.org/

.. code-block:: none
    :caption: Developer Certificate of Origin

    Developer Certificate of Origin
    Version 1.1

    Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
    1 Letterman Drive
    Suite D4700
    San Francisco, CA, 94129

    Everyone is permitted to copy and distribute verbatim copies of this
    license document, but changing it is not allowed.


    Developer's Certificate of Origin 1.1

    By making a contribution to this project, I certify that:

    (a) The contribution was created in whole or in part by me and I
        have the right to submit it under the open source license
        indicated in the file; or

    (b) The contribution is based upon previous work that, to the best
        of my knowledge, is covered under an appropriate open source
        license and I have the right under that license to submit that
        work with modifications, whether created in whole or in part
        by me, under the same open source license (unless I am
        permitted to submit under a different license), as indicated
        in the file; or

    (c) The contribution was provided directly to me by some other
        person who certified (a), (b) or (c) and I have not modified
        it.

    (d) I understand and agree that this project and the contribution
        are public and that a record of the contribution (including all
        personal information I submit with it, including my sign-off) is
        maintained indefinitely and may be redistributed consistent with
        this project or the open source license(s) involved.

Be mindful about the sign-off rules on the projects you are contributing to
and make sure you understand what the sign-off means in case the project you
are contributing to has a document similar to this.

Refer to the manpage for ``git-interpret-trailers`` for more details on
trailers.


Final tips on commit messages
=============================

* **Resist the urge to use** ``git commit -m 'My commit message'``

  While it may seem handy, it promotes a bad habit of writing unthoughtful
  commit messages. By editing your commit message in a full editor you will
  spend more time thinking about your commit message, often producing higher
  quality messages.

* **Spend time reviewing code yourself**

  If you are actively participating in a project, spend some time reviewing
  code on that project even if you are not a maintainer or committer on the
  project. This is the best way for you to quickly learn the best practices of
  not only the project but also what we discussed here as it is easier to
  understand the hardships of a code reviewer if you are one yourself.
