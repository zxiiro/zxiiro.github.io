---
layout: post
title: Reporting in Freeseer
categories:
- fosslc
- freeseer
tags:
- freeseer
- python
status: publish
type: post
published: true
meta:
  _wpas_done_facebook: '1'
  _wpas_done_twitter: '1'
  _elasticsearch_indexed_on: '2012-06-24 01:53:32'
---
Occasionally when doing a recording issues could occur such as the audio not working, video is not working or perhaps the presenter does not wish to be recorded. After a conference it is difficult for one person to know which talks have issues, especially if 100s of talks are recorded at the event.

To solve this issue Freeseer comes with a basic reporting tool that will allow the person recording to report issues with their talks inside the application. This will allow whomever is uploading the videos after the talk to quickly scan through and find which videos have issues.

To access the reporting interface, with freeseer-record open simply click <strong>Help &gt; Report</strong>. The reporting interface will open a basic form for the currently selected talk.

<a href="/assets/blog/2012-06/report-1.png"><img class="img-responsive img-thumbnail" title="Reporting Interface" src="/assets/blog/2012-06/report-1.png" alt="Reporting Interface" width="300" height="115" /></a>

The form has 3 fields which need to be assessed by the reporter.

<ol>
	<li>A comment describing the issue seen.</li>
	<li>A type of issue, one of "No Issue", "No Audio", "No Video", and "No Audio/Video".</li>
	<li>A checkbox indicating if a Release Form was received or not.</li>
</ol>

The last item is a new feature we added for events where presenters must sign a release form indicating they are giving permission to record their talk. Typicially this option is used with the "No Issue" flag unless there are issues with the recording.

&nbsp;

Freeseer also provides a <strong>Report Editor</strong> which will allow the organizer after the event to quickly browse through all the reports and find out which ones have issues.

<a href="/assets/blog/2012-06/report-2.png"><img class="img-responsive img-thumbnail" title="Report Editor" src="/assets/blog/2012-06/report-2.png" alt="Report Editor" width="300" height="128" /></a>

&nbsp;
