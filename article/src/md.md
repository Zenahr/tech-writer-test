# Hacker News API Guide

![](./media/1.jpg)

>**Disclaimer** <br> This is an unofficial guide to the HackerNews API. The author is not affiliated with HN in any official function.

## Getting Started

This tutorial is meant as a quick step-by-step guide to get started using the [HN API](https://github.com/HackerNews/API) whilst also teaching some fundamental things about APIs and introducing useful tools for testing APIs. This tutorial is mainly geared towards junior developers.

## Hacker News

[Hacker News](https://news.ycombinator.com/) is a social news website focusing on computer science and entrepreneurship. It follows the "anything that gratifies one's intellectual curiosity" slogan. If you haven't been on Hacker News before, feel free to pause this guide and stop by to get a feel of what we're going to work with. (Source: [Wiki](https://en.wikipedia.org/wiki/Hacker_News))

### Types of Content

Content posted on Hacker News can be put into one of the following categories:

- Stories
- Jobs
- Comments
- Ask Hacker News

We will learn how to get the content using a

## Precourse on what APIs are
- Disclaimer (You can skip this if you have worked with APIs before)
- You talk with web APIs using HTTP clients. The windows command-line comes with curl built-in, but most popular programming languages have plug-and-play HTTP client libraries.
- Explain in quick sentences what APIs generally are
- Now a quick intro to Web APIs and the Restful paradigm

## Exploring the API

- Intro to the API (open/closed?) (not restful)
- The API is a collection of HTTP RPC-style methods using following URL building principle:
`https://hacker-news.firebaseio.com/v0/METHOD_FAMILY.method`
example:
`https://hacker-news.firebaseio.com/v0/beststories.json`

>For anyone interested in reading more about the differences between REST and RPC I recommend [this article](https://www.smashingmagazine.com/2016/09/understanding-rest-and-rpc-for-http-apis/) by Phil Sturgeon.


### Methods
- Introductory text explaining where and how I obtained the table
- Table of endpoints itself

The current API does not follow the Restful paradigm. Everything is an item. There are no semantic endpoints such as `api/stories`,  or `api/jobs` except `api/users`. The only way to only get one type of item is by using the following 

|Method|Description|Endpoint|
|---|---|---|
|`beststories.json`|||
|`maxitem.json`|get item with currently largest id|https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty|
|`topstories.json`|Get 500 top stories|https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty|
|`newstories.json`|Get 500 latest stories (Also contains jobs)|https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty|
|`beststories.json`|Get 500 best voted stories sorted by votes in descending order|https://hacker-news.firebaseio.com/v0/beststories.json|
|`askstories.json`|Get latest Ask Stories|https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty|
|`showstories.json`|Get latest Show Stories|https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty|
|`jobstories.json`|Get latest Job Stories|https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty|
|`updates.json`|Get latest items that have been updated (including profiles)|https://hacker-news.firebaseio.com/v0/updates.json?print=pretty|

## Example Scenario

- Explain what we want to do
- Show results of using 
https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty
- explain API parameters (beststories is a an object and we use . notation here to access the objects json property)

## Integration example (webapp architecture and use-case)

## Limitations

The current API is limited in its use. It only supports ¼ of standard `CRUD` API functionality. This means one can't Create(`C`), Update(`U`) or Delete(`C`) but only Read(`R`) database entries. It also does not support [pagination](https://developer.atlassian.com/server/confluence/pagination-in-the-rest-api/).

## Outro

I have created this repo and a public Postman Docs site containing everything we went through in case you'd like to use this as a resource for further learning or to build the next Hacker News Reader App.