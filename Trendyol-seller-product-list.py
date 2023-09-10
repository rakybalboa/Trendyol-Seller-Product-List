import requests
import math

def seller_product_list(seller_id):
    page=1
    total_page = calculate_total_page(seller_id)
    headers = {
        'authority': 'public.trendyol.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfbmFtZSI6ImJhc3R1cmtyYW1hemFuQGdtYWlsLmNvbSIsInN1YiI6ImJhc3R1cmtyYW1hemFuQGdtYWlsLmNvbSIsImVtYWlsIjoiYmFzdHVya3JhbWF6YW5AZ21haWwuY29tIiwicm9sZSI6InVzZXIiLCJ1c2VySWQiOiIzMDU0ODk5NyIsIlN0YW5kYXJkVXNlciI6IjAiLCJhdHdydG1rIjoiYTAwZTg0YjMtNjA4ZC00NzA4LTgwZjQtN2JlNzMxNmRmYjJhIiwiaXNzIjoiYXV0aC50cmVuZHlvbC5jb20iLCJhdWQiOiJzYkF5ell0WCtqaGVMNGlmVld5NXR5TU9MUEpXQnJrYSIsImV4cCI6MTc4MTU4ODY2MiwibmJmIjoxNjIzODAzOTAyfQ.Hzsp09dyZadoUBweZP5L41jqFuVc_CMFsmMgh0KaERw',
        'origin': 'https://www.trendyol.com',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    params = {
        'mid': f'{seller_id}',
        'os': '1',
        'pi': f'{page}',
        'culture': 'tr-TR',
        'userGenderId': '2',
        'pId': '0',
        'isLegalRequirementConfirmed': 'false',
        'searchStrategyType': 'DEFAULT',
        'productStampType': 'TypeA',
        'scoringAlgorithmId': '2',
        'fixSlotProductAdsIncluded': 'true',
        'searchAbDecider': 'Suggestion_A,Relevancy_1,FilterRelevancy_1,ListingScoringAlgorithmId_1,Smartlisting_70,SuggestionBadges_B,ProductGroupTopPerformer_B,OpenFilterToggle_2,BadgeBoost_A,RF_1,PastSearches_B,SuggestionPopularCTR_B',
    }

    for page in (n+1 for n in range(total_page)):
        response = requests.get(
            'https://public.trendyol.com/discovery-web-searchgw-service/v2/api/infinite-scroll/sr',
            params=params,
            headers=headers,
        )

        json_response = response.json()['result']['products']
        
        for product in json_response:
            product_specs = {}
            print("https://www.trendyol.com/"+product['url'].split("?")[0])
        print("Page number is",page)
        

def calculate_total_page(seller_id):

    response = requests.get(
        f'https://www.trendyol.com/sr?mid={seller_id}', 'html.parser'
    )
    
    total_product = int(response.text.split("araması için ")[1].split(" sonuç")[0])
    total_page = math.ceil(total_product / 24)
    
    return total_page
        

seller_product_list(input("6 haneli satıcı id giriniz: "))