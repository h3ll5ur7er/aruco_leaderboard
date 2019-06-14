# IO.Swagger.Api.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAllCarsEndpoint**](DefaultApi.md#getallcarsendpoint) | **GET** /car | 
[**GetAllCategoriesEndpoint**](DefaultApi.md#getallcategoriesendpoint) | **GET** /category | 
[**GetAllDriversEndpoint**](DefaultApi.md#getalldriversendpoint) | **GET** /driver | 
[**GetAllEventsEndpoint**](DefaultApi.md#getalleventsendpoint) | **GET** /event | 
[**GetAllLapEndpoint**](DefaultApi.md#getalllapendpoint) | **GET** /lap | 
[**GetAllRacesEndpoint**](DefaultApi.md#getallracesendpoint) | **GET** /race | 
[**GetAllResultsEndpoint**](DefaultApi.md#getallresultsendpoint) | **GET** /result | 
[**GetAllTeamsEndpoint**](DefaultApi.md#getallteamsendpoint) | **GET** /team | 
[**GetMarkerGeneratorEndpoint**](DefaultApi.md#getmarkergeneratorendpoint) | **GET** /generate/marker/{marker_id} | 
[**GetOneCarEndpoint**](DefaultApi.md#getonecarendpoint) | **GET** /car/{id} | 
[**GetOneCategoryEndpoint**](DefaultApi.md#getonecategoryendpoint) | **GET** /category/{id} | 
[**GetOneDriverEndpoint**](DefaultApi.md#getonedriverendpoint) | **GET** /driver/{id} | 
[**GetOneEventEndpoint**](DefaultApi.md#getoneeventendpoint) | **GET** /event/{id} | 
[**GetOneLapEndpoint**](DefaultApi.md#getonelapendpoint) | **GET** /lap/{id} | 
[**GetOneRaceEndpoint**](DefaultApi.md#getoneraceendpoint) | **GET** /race/{id} | 
[**GetOneResultEndpoint**](DefaultApi.md#getoneresultendpoint) | **GET** /result/{id} | 
[**GetOneTeamsEndpoint**](DefaultApi.md#getoneteamsendpoint) | **GET** /team/{id} | 
[**PostAllCarsEndpoint**](DefaultApi.md#postallcarsendpoint) | **POST** /car | 
[**PostAllCategoriesEndpoint**](DefaultApi.md#postallcategoriesendpoint) | **POST** /category | 
[**PostAllDriversEndpoint**](DefaultApi.md#postalldriversendpoint) | **POST** /driver | 
[**PostAllEventsEndpoint**](DefaultApi.md#postalleventsendpoint) | **POST** /event | 
[**PostAllLapEndpoint**](DefaultApi.md#postalllapendpoint) | **POST** /lap | 
[**PostAllRacesEndpoint**](DefaultApi.md#postallracesendpoint) | **POST** /race | 
[**PostAllResultsEndpoint**](DefaultApi.md#postallresultsendpoint) | **POST** /result | 
[**PostAllTeamsEndpoint**](DefaultApi.md#postallteamsendpoint) | **POST** /team | 
[**PostMarkerDetectorEndpoint**](DefaultApi.md#postmarkerdetectorendpoint) | **POST** /detect/marker | 
[**PostOneCarEndpoint**](DefaultApi.md#postonecarendpoint) | **POST** /car/{id} | 
[**PostOneCategoryEndpoint**](DefaultApi.md#postonecategoryendpoint) | **POST** /category/{id} | 
[**PostOneDriverEndpoint**](DefaultApi.md#postonedriverendpoint) | **POST** /driver/{id} | 
[**PostOneEventEndpoint**](DefaultApi.md#postoneeventendpoint) | **POST** /event/{id} | 
[**PostOneLapEndpoint**](DefaultApi.md#postonelapendpoint) | **POST** /lap/{id} | 
[**PostOneRaceEndpoint**](DefaultApi.md#postoneraceendpoint) | **POST** /race/{id} | 
[**PostOneResultEndpoint**](DefaultApi.md#postoneresultendpoint) | **POST** /result/{id} | 
[**PostOneTeamsEndpoint**](DefaultApi.md#postoneteamsendpoint) | **POST** /team/{id} | 


<a name="getallcarsendpoint"></a>
# **GetAllCarsEndpoint**
> Cars GetAllCarsEndpoint (string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetAllCarsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Cars result = apiInstance.GetAllCarsEndpoint(xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetAllCarsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Cars**](Cars.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getallcategoriesendpoint"></a>
# **GetAllCategoriesEndpoint**
> Categories GetAllCategoriesEndpoint (string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetAllCategoriesEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Categories result = apiInstance.GetAllCategoriesEndpoint(xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetAllCategoriesEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Categories**](Categories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getalldriversendpoint"></a>
# **GetAllDriversEndpoint**
> Drivers GetAllDriversEndpoint (string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetAllDriversEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Drivers result = apiInstance.GetAllDriversEndpoint(xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetAllDriversEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Drivers**](Drivers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getalleventsendpoint"></a>
# **GetAllEventsEndpoint**
> Events GetAllEventsEndpoint (string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetAllEventsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Events result = apiInstance.GetAllEventsEndpoint(xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetAllEventsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getalllapendpoint"></a>
# **GetAllLapEndpoint**
> Laps GetAllLapEndpoint (string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetAllLapEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Laps result = apiInstance.GetAllLapEndpoint(xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetAllLapEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Laps**](Laps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getallracesendpoint"></a>
# **GetAllRacesEndpoint**
> Races GetAllRacesEndpoint (string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetAllRacesEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Races result = apiInstance.GetAllRacesEndpoint(xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetAllRacesEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Races**](Races.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getallresultsendpoint"></a>
# **GetAllResultsEndpoint**
> Results GetAllResultsEndpoint (string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetAllResultsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Results result = apiInstance.GetAllResultsEndpoint(xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetAllResultsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Results**](Results.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getallteamsendpoint"></a>
# **GetAllTeamsEndpoint**
> Teams GetAllTeamsEndpoint (string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetAllTeamsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Teams result = apiInstance.GetAllTeamsEndpoint(xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetAllTeamsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Teams**](Teams.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getmarkergeneratorendpoint"></a>
# **GetMarkerGeneratorEndpoint**
> void GetMarkerGeneratorEndpoint (int? markerId)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetMarkerGeneratorEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var markerId = 56;  // int? | 

            try
            {
                apiInstance.GetMarkerGeneratorEndpoint(markerId);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetMarkerGeneratorEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **markerId** | **int?**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getonecarendpoint"></a>
# **GetOneCarEndpoint**
> Car GetOneCarEndpoint (int? id, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetOneCarEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Car result = apiInstance.GetOneCarEndpoint(id, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetOneCarEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Car**](Car.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getonecategoryendpoint"></a>
# **GetOneCategoryEndpoint**
> Category GetOneCategoryEndpoint (int? id, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetOneCategoryEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Category result = apiInstance.GetOneCategoryEndpoint(id, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetOneCategoryEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getonedriverendpoint"></a>
# **GetOneDriverEndpoint**
> Driver GetOneDriverEndpoint (int? id, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetOneDriverEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Driver result = apiInstance.GetOneDriverEndpoint(id, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetOneDriverEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Driver**](Driver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getoneeventendpoint"></a>
# **GetOneEventEndpoint**
> Event GetOneEventEndpoint (int? id, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetOneEventEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Event result = apiInstance.GetOneEventEndpoint(id, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetOneEventEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getonelapendpoint"></a>
# **GetOneLapEndpoint**
> Lap GetOneLapEndpoint (int? id, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetOneLapEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Lap result = apiInstance.GetOneLapEndpoint(id, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetOneLapEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Lap**](Lap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getoneraceendpoint"></a>
# **GetOneRaceEndpoint**
> Race GetOneRaceEndpoint (int? id, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetOneRaceEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Race result = apiInstance.GetOneRaceEndpoint(id, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetOneRaceEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Race**](Race.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getoneresultendpoint"></a>
# **GetOneResultEndpoint**
> Result GetOneResultEndpoint (int? id, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetOneResultEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Result result = apiInstance.GetOneResultEndpoint(id, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetOneResultEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getoneteamsendpoint"></a>
# **GetOneTeamsEndpoint**
> Team GetOneTeamsEndpoint (int? id, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetOneTeamsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Team result = apiInstance.GetOneTeamsEndpoint(id, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetOneTeamsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postallcarsendpoint"></a>
# **PostAllCarsEndpoint**
> Car PostAllCarsEndpoint (Car payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostAllCarsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var payload = new Car(); // Car | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Car result = apiInstance.PostAllCarsEndpoint(payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostAllCarsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Car**](Car.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Car**](Car.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postallcategoriesendpoint"></a>
# **PostAllCategoriesEndpoint**
> Category PostAllCategoriesEndpoint (Category payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostAllCategoriesEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var payload = new Category(); // Category | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Category result = apiInstance.PostAllCategoriesEndpoint(payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostAllCategoriesEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Category**](Category.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postalldriversendpoint"></a>
# **PostAllDriversEndpoint**
> Driver PostAllDriversEndpoint (Driver payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostAllDriversEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var payload = new Driver(); // Driver | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Driver result = apiInstance.PostAllDriversEndpoint(payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostAllDriversEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Driver**](Driver.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Driver**](Driver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postalleventsendpoint"></a>
# **PostAllEventsEndpoint**
> Event PostAllEventsEndpoint (Event payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostAllEventsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var payload = new Event(); // Event | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Event result = apiInstance.PostAllEventsEndpoint(payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostAllEventsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Event**](Event.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postalllapendpoint"></a>
# **PostAllLapEndpoint**
> Lap PostAllLapEndpoint (Lap payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostAllLapEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var payload = new Lap(); // Lap | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Lap result = apiInstance.PostAllLapEndpoint(payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostAllLapEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Lap**](Lap.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Lap**](Lap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postallracesendpoint"></a>
# **PostAllRacesEndpoint**
> Race PostAllRacesEndpoint (Race payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostAllRacesEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var payload = new Race(); // Race | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Race result = apiInstance.PostAllRacesEndpoint(payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostAllRacesEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Race**](Race.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Race**](Race.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postallresultsendpoint"></a>
# **PostAllResultsEndpoint**
> Result PostAllResultsEndpoint (Result payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostAllResultsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var payload = new Result(); // Result | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Result result = apiInstance.PostAllResultsEndpoint(payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostAllResultsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Result**](Result.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postallteamsendpoint"></a>
# **PostAllTeamsEndpoint**
> Team PostAllTeamsEndpoint (Team payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostAllTeamsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var payload = new Team(); // Team | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Team result = apiInstance.PostAllTeamsEndpoint(payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostAllTeamsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Team**](Team.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postmarkerdetectorendpoint"></a>
# **PostMarkerDetectorEndpoint**
> Markers PostMarkerDetectorEndpoint (System.IO.Stream file, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostMarkerDetectorEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var file = new System.IO.Stream(); // System.IO.Stream | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Markers result = apiInstance.PostMarkerDetectorEndpoint(file, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostMarkerDetectorEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **System.IO.Stream**|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Markers**](Markers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postonecarendpoint"></a>
# **PostOneCarEndpoint**
> Car PostOneCarEndpoint (int? id, Car payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostOneCarEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var payload = new Car(); // Car | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Car result = apiInstance.PostOneCarEndpoint(id, payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostOneCarEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **payload** | [**Car**](Car.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Car**](Car.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postonecategoryendpoint"></a>
# **PostOneCategoryEndpoint**
> Category PostOneCategoryEndpoint (int? id, Category payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostOneCategoryEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var payload = new Category(); // Category | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Category result = apiInstance.PostOneCategoryEndpoint(id, payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostOneCategoryEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **payload** | [**Category**](Category.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postonedriverendpoint"></a>
# **PostOneDriverEndpoint**
> Driver PostOneDriverEndpoint (int? id, Driver payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostOneDriverEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var payload = new Driver(); // Driver | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Driver result = apiInstance.PostOneDriverEndpoint(id, payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostOneDriverEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **payload** | [**Driver**](Driver.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Driver**](Driver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postoneeventendpoint"></a>
# **PostOneEventEndpoint**
> Event PostOneEventEndpoint (int? id, Event payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostOneEventEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var payload = new Event(); // Event | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Event result = apiInstance.PostOneEventEndpoint(id, payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostOneEventEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **payload** | [**Event**](Event.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postonelapendpoint"></a>
# **PostOneLapEndpoint**
> Lap PostOneLapEndpoint (int? id, Lap payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostOneLapEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var payload = new Lap(); // Lap | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Lap result = apiInstance.PostOneLapEndpoint(id, payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostOneLapEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **payload** | [**Lap**](Lap.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Lap**](Lap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postoneraceendpoint"></a>
# **PostOneRaceEndpoint**
> Race PostOneRaceEndpoint (int? id, Race payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostOneRaceEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var payload = new Race(); // Race | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Race result = apiInstance.PostOneRaceEndpoint(id, payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostOneRaceEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **payload** | [**Race**](Race.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Race**](Race.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postoneresultendpoint"></a>
# **PostOneResultEndpoint**
> Result PostOneResultEndpoint (int? id, Result payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostOneResultEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var payload = new Result(); // Result | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Result result = apiInstance.PostOneResultEndpoint(id, payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostOneResultEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **payload** | [**Result**](Result.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="postoneteamsendpoint"></a>
# **PostOneTeamsEndpoint**
> Team PostOneTeamsEndpoint (int? id, Team payload, string xFields = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PostOneTeamsEndpointExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var id = 56;  // int? | 
            var payload = new Team(); // Team | 
            var xFields = xFields_example;  // string | An optional fields mask (optional) 

            try
            {
                Team result = apiInstance.PostOneTeamsEndpoint(id, payload, xFields);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PostOneTeamsEndpoint: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**|  | 
 **payload** | [**Team**](Team.md)|  | 
 **xFields** | **string**| An optional fields mask | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

