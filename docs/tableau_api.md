# Tableau REST API Methods used in the project

## Author(s)
- [Mustafa Aljumayli](https://github.com/id-mustafa)

## Description
To capture data about from our Tableau Server, we call on REST APIs to help us extract the information we need. This document will outline the REST API methods used, their sample output and what information they're supposed to give us and how they've been used to fulfill our requirements.


## [Obtaining Credentials Token](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_authentication.htm#sign_in)

Purpose: to gain access to your Tableau site's API so that you may begin making requests.

This API call is how you'll be able to find the credentials token and site ID. You need your Tableau Username, Password, and site's Content URL to proceed with making this call. 

To find your site's content url, you can login to Tableau Server and select the site you'd like to pull data from. Then once you're logged in, you can look at the URL in the browser. It should look something like this:

https://tableau.example.edu/#/site/CONTENT-URL/home

As you can see, this is the easiest way to get the site's content url. 

### Available Endpoint(s)

* POST https://MY_SERVER/api/api-version/auth/signin

### Parameter Values
* api-version:	The version of the API to use, such as 3.22. For more information, see [REST API and Resource Versions](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm).

### Headers
| Key               | Value
|-------------------|-----------------
| Content-Type      | application/xml

The Content-Type header allows you to specify how you want the response.

### Request Body

```xml
<tsRequest>
    <credentials name="TABLEAU USERNAME" password="TABLEAU PASSWORD">
        <site contentUrl="CONTENT URL"/>
    </credentials>
</tsRequest>
```


### Response Body
```xml
<?xml version='1.0' encoding='UTF-8'?>
<tsResponse xmlns="http://tableau.com/api" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://tableau.com/api https://help.tableau.com/samples/en-us/rest_api/ts-api_3_21.xsd">
    <credentials token="CREDENTIALS TOKEN">
        <site id="SITE ID" contentUrl="CONTENT URL"/>
        <user id="USER ID"/>
    </credentials>
</tsResponse>
```
### [HTTP Status Codes and Their Meanings](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_authentication.htm#sign_in)

* 200 = Successful request
* 400 = Bad request
* 401 = Login Error
* 405 = Invalid request method (AKA request type was not 'POST')

For more information about HTTP Status Codes, please click [here](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_authentication.htm#sign_in) to get a more detailed explanation for this API call.

## [Query Workbooks for Site](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_workbooks_and_views.htm#query_workbooks_for_site)

Purpose: Returns the workbooks on a site.

If the user is not an administrator, the method returns just the workbooks that the user has permissions to view. Handling pagination is important in order to obtain all workbooks.

### Available Endpoint(s)
* GET /api/api-version/sites/site-id/workbooks

* GET /api/api-version/sites/site-id/workbooks?filter=filter-expression

* GET /api/api-version/sites/site-id/workbooks?sort=sort-expression

* GET /api/api-version/sites/site-id/workbooks?pageSize=page-size&pageNumber=page-number

* GET /api/api-version/sites/site-id/workbooks?fields=field-expression

### Parameter Values
* api-version:	The version of the API to use, such as 3.22. For more information, see REST API and Resource Versions. UNC SOG is 3.21

* site-id:	The ID of the site that contains the workbooks. UNC SOG's site-id can be retrieved by obtaining credentials.

* page-size	(Optional): The number of items to return in one response. The minimum is 1. The maximum is 1000. The default is 100. For more information, see Paginating Results.

* page-number (Optional): The offset for paging. The default is 1. For more information, see Paginating Results.

* filter-expression	(Optional): An expression that lets you specify a subset of data sources to return. You can filter on predefined fields such as name and updatedAt. You can include multiple filter expressions. For more information, see Filtering and Sorting.

* sort-expression (Optional): An expression that lets you specify the order in which user information is returned. If you do not specify a sort expression, the sort order of the information that's returned is undefined. For more information, see Filtering and Sorting.

* field-expression (Optional): An expression that lets you specify the set of available fields to return. You can qualify the return values based upon predefined keywords such as _all_ or _default_, and you can specify individual fields for the data sources or other supported resources. You can include multiple field expressions in a request. For more information, see Using Fields in the Rest API.

### Headers
| Key               | Value
|-------------------|-----------------
| X-Tableau-Auth    | CREDENTIALS_TOKEN

The Tableau authentication header. The value is a credentials token from a Tableau server's response to an authentication request. The Content-Type and Accept headers should be the mediatype of the request and response except in cases where you want to explicitly allow other versions of the resource.

### Response Body
```xml
<tsResponse>
  <pagination pageNumber="page-number"
     pageSize="page-size"
     totalAvailable="total-available" />
  <workbooks>
    <workbook id="workbook-id"
		name="name"
		description ="workbook-description"
		webpageurl="workbook-webpageurl"
		contentUrl="content-url"
        showTabs="show-tabs-flag"
        size="size-in-megabytes"
        createdAt="datetime-created"
	    updatedAt="datetime-updated"
	    defaultViewId="default-view-id" >
	      <project id="project-id" name="project-name" />
	      <owner id="user-id" />
	      <tags>
	        <tag label="tag"/>
	        ... additional tags ...
	     </tags>
	<dataAccelerationConfig accelerationEnabled="accelerationEnabled" lastUpdatedAt="update-date-time" accelerationStatus="accelerationStatus" />
   </workbook>
   ... additional workbooks ...
  </workbooks>
</tsResponse>
```
### [HTTP Status Codes and Their Meanings](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_workbooks_and_views.htm#query_workbooks_for_site)

* 200 = Successful request
* 400 = Invalid Page Number or Page Size
* 403 = Page Size exceeds the 1000 limit or the requestor doesn't have the necessary read permissions
* 404 = Site not found or incorrect endpoint
* 405 = Invalid request method (AKA request type was not 'Get')

## [Query Data Sources](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_data_sources.htm#query_data_sources)

Purpose: Returns a list of published data sources on the specified site, with optional parameters for specifying the paging of large results. To get a list of data sources embedded in a workbook, use the Query Workbook Connections method.

### Available Endpoint(s)

* GET /api/api-version/sites/site-id/datasources

* GET /api/api-version/sites/site-id/datasources?pageSize=page-size&pageNumber=page-number

* GET /api/api-version/sites/site-id/datasources?filter=filter-expression

* GET /api/api-version/sites/site-id/datasources?sort=sort-expression

* GET /api/api-version/sites/site-id/datasources?fields=field-expression

### Parameter Values
* api-version:	The version of the API to use, such as 3.22. For more information, see REST API and Resource Versions. UNC SOG is 3.21

* site-id:	The ID of the site that contains the data sources. UNC SOG's site-id can be retrieved by obtaining credentials.

* page-size	(Optional): The number of items to return in one response. The minimum is 1. The maximum is 1000. The default is 100. For more information, see Paginating Results.
page-number	(Optional) The offset for paging. The default is 1. For more information, see Paginating Results.

* filter-expression	(Optional): An expression that lets you specify a subset of data sources to return. You can filter on predefined fields such as name and updatedAt. You can include multiple filter expressions. For more information, see Filtering and Sorting.

* sort-expression (Optional): An expression that lets you specify the order in which user information is returned. If you do not specify a sort expression, the sort order of the information that's returned is undefined. For more information, see Filtering and Sorting.

* field-expression (Optional): An expression that lets you specify the set of available fields to return. You can qualify the return values based upon predefined keywords such as _all_ or _default_, and you can specify individual fields for the data sources or other supported resources. You can include multiple field expressions in a request. For more information, see Using Fields in the Rest API.

### Headers
| Key               | Value
|-------------------|-----------------
| X-Tableau-Auth    | CREDENTIALS_TOKEN

The Tableau authentication header. The value is a credentials token from a Tableau server's response to an authentication request. The Content-Type and Accept headers should be the mediatype of the request and response except in cases where you want to explicitly allow other versions of the resource.

### Response Body
```xml
<tsResponse>
  <pagination pageNumber="pageNumber" pageSize="page-size"
    totalAvailable="total-available" />
  <datasources>
    <datasource id="datasource1-id"
      description="data-source-description"
      name="datasource-name"
      size="datasource-size"
      type="datasource-type"
      contentUrl="datasource-content-url"
      createdAt="datetime-created"
      updatedAt="datetime-updated"
      encryptExtracts="encrypt-extracts-flag"
      hasExtracts="has-extracts-flag"
      isCertified="is-certified-flag"
      useRemoteQueryAgent="use-remote-query-agent-flag"
      webpageUrl="datasource-webpage-url"  >
	    <project id="project-id" name="project-name" />
        <owner id="datasource-owner-id" />
        <tags>
          <tag label="tag"/>
          ... additional tags ...
        </tags>
    </datasource>
    ... additional data sources ...
  </datasources>
</tsResponse>
``` 

### [HTTP Status Codes and Their Meanings](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_data_sources.htm#query_data_sources)

* 200 = Successful request
* 400 = Invalid Page Number or Page Size
* 403 = Page Size exceeds the 1000 limit or the requestor doesn't have the necessary read permissions
* 404 = Site not found or incorrect endpoint
* 405 = Invalid request method (AKA request type was not 'Get')

## [Get Usage Statistics for Content Item](https://help.tableau.com/current/api/rest_api/en-us/REST/TAG/index.html#tag/Content-Exploration-Methods/operation/UsageStatsService_GetUsageStats)

Purpose: Returns hits or in other words, the physical views for a workbook or datasource. This is not to be confused with views because a view in tableau refers to a visualization in a workbook. Hits are what Tableau uses to refer to the usage statistic. This goes back and gets usage for the past 12 months.

### Available Endpoint(s)
* GET https://tableau.example.com/api/-/content/usage-stats/{type}/{luid}

### Parameter Values
* type: A string that specifies the type of content item. Could be 'datasources', 'workbooks;, or 'flows'

* luid: Universal string Identifier for content items in Tableau's API Schema

### Headers
| Key               | Value
|-------------------|-----------------
| X-Tableau-Auth    | CREDENTIALS_TOKEN

The Tableau authentication header. The value is a credentials token from a Tableau server's response to an authentication request. The Content-Type and Accept headers should be the mediatype of the request and response except in cases where you want to explicitly allow other versions of the resource.

### Response Body
```JSON
{
  "hitsTotal": 0,
  "hitsLastTwoWeeksTotal": 0,
  "hitsLastOneMonthTotal": 0,
  "hitsLastThreeMonthsTotal": 0,
  "hitsLastTwelveMonthsTotal": 0
}
```

### [HTTP Status Codes and Their Meanings](https://help.tableau.com/current/api/rest_api/en-us/REST/TAG/index.html#tag/Content-Exploration-Methods/operation/UsageStatsService_GetUsageStats)

* 200 = Successful request
* 400 = Usage statistics are not supported for the provided content type.
* 401 = Unable to authenticate user. Credentials are missing or invalid.
* 404 = Invalid request. The requested resource could not be found.
* 500 = Unknown error. There was an internal server error.
* 503 = Service unavailable.


## [Query Published Datasource Connections](https://github.com/tableau/metadata-api-samples/blob/master/samples/quickstart-workbooks.graphql)

Purpose: Returns a list of data connections for the specific datasource and some connection data.

### Available Endpoint(s)

* POST https://{TABLEAU_SERVER}/api/metadata/graphql

### Parameter Values
* Tableau Server: The domain for your organization specifies which organization's metadata api you are trying to make calls to.

### Headers
| Key               | Value
|-------------------|-----------------
| X-Tableau-Auth    | CREDENTIALS_TOKEN

The Tableau authentication header. The value is a credentials token from a Tableau server's response to an authentication request. The Content-Type and Accept headers should be the mediatype of the request and response except in cases where you want to explicitly allow other versions of the resource.

### Request Body
```graphql
query published_datasources{
  publishedDatasources {
    luid
    name
    extractLastRefreshTime
    downstreamWorkbooks{
        luid
        name 
    }
    upstreamDatabases {
        luid
        name
    }
    isCertified
    certifier {
      luid
      name
    }
    certifierDisplayName
  }
}
```

### Response Body
```json
"data": {
    "publishedDatasources": [
        {
            "luid": "{datasource_id}",
            "name": "{datasource_name}",
            "extractLastRefreshTime": null,
            "downstreamWorkbooks": [
                {
                    "luid": "{workbook_id}",
                    "name": "{workbook_name}"
                }
            ],
            "upstreamDatabases": [
                {
                    "luid": "{database_id}",
                    "name": "{database_name}"
                }
            ],
            "isCertified": false,
            "certifier": null,
            "certifierDisplayName": null
        }
    ]
}
```

### [HTTP Status Codes and Their Meanings](https://github.com/tableau/metadata-api-samples/blob/master/samples/quickstart-workbooks.graphql)

* 200 = Successful request
* 403 = The requestor doesn't have the necessary read permissions
* 404 = Site, workbook, or endpoint not found
* 405 = Invalid request method (AKA request type was not 'Get')

 __authors__ = ["Mustafa Aljumayli"]