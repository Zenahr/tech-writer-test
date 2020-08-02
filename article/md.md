# Hacker News API Guide

## Getting Started

- What do we want to do
- What audience this is addressing (level of expertise)
- what tech stack we'll be using for demonstration purposes
- Where can we find additional resources (Postman API package, code examples) if any? (Link to public GitHub repo)

## Hacker News
- What is the website about?
- What kind of content does exist? (Comments, Stories etc.)

## Precourse on what APIs are
- Disclaimer (You can skip this if you have worked with APIs before)
- You talk with web APIs using HTTP clients. The windows command-line comes with curl built-in, but most popular programming languages have plug-and-play HTTP client libraries.
- Explain in quick sentences what APIs generally are
- Now a quick intro to Web APIs and the Restful paradigm

## Exploring the API

- Intro to the API (open/closed?) (not restful)

### Endpoints
- Introductory text explaining where and how I obtained the table
- Table of endpoints itself

The current API does not follow the Restful paradigm. Everything is an item. There are no semantic endpoints such as `api/stories`,  or `api/jobs` except `api/users`. The only way to only get one type of item is by using the following 

|endpoint|Description|Example|
|---|---|---|
|||

## Example Scenario

- Explain what we want to do
- Show results of hitting endpoints
https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty
- explain API parameters (beststories is a an object and we use . notation here to access the objects json property)

## Integration example (webapp architecture and use-case)