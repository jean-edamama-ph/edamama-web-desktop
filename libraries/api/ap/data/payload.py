import json
class login:
    """LOGIN"""
    def login():
        dictPayload = {"email":"jean@edamama.ph","password":"Edamama@123!"}
        return dictPayload
    
    
    
    
    
    
class orders:
    """ORDERS"""
    def dictUpdateDetails(dictData):
        return {"orderId": dictData["strID"],
                "deliveryAddress": {
                    "fullName": dictData["strFullName"],
                    "zipCode": dictData["strZipCode"],
                    "city": {
                        "name": dictData["strCityName"],
                        "_id": "609fc3a7b1380627d48c7519",
                        "regionId": "5dc5309b73a7ecd817f5b781"
                    },
                    "landmark": dictData["strLandmark"],
                    "buildingNumber": dictData["strBuildingNumber"],
                    "phoneNumber": dictData["strPhoneNumber"],
                    "isDefault": dictData["strIsDefault"],
                    "region": {
                        "_id": "5dc5309b73a7ecd817f5b781",
                        "name": dictData["strRegionName"]
                    },
                    "barangay": {
                        "name": dictData["strBarangayName"],
                        "_id": "609fc434b1380627d48d0afb",
                        "cityId": "609fc3a7b1380627d48c7519"
                    }
                },
                "email": dictData["strEmail"]
            }
        
    
    
    
    
class subcription:
    """SUBSCRIPTION"""
    # def cancel(strSubscription):
    #     dictPayload = {"_id":"f'{strSubscription}'"}
    #     return dictPayload

    def cancel(strSubscription):
          return {"_id":strSubscription}
      
      
      
      
      
class scheduler:
    """DISCOUNT SCHEDULER"""
    def dictCancelPayload(strUUID):
        return {"uuid":strUUID}
    
    
    class rs:
        """RS"""
        arrPUPayload = [{"sku":"EDA-42833","sellerDiscountPercentage":9,"totalDiscountPercentage":10},{"sku":"EDA-42834","sellerDiscountPercentage":9,"totalDiscountPercentage":10}]
        
        def dictPDPayload(dictData):
            return {"name": dictData["strName"],
                    "discountType": dictData["strDiscountType"],
                    "isOnSpotlight": dictData["blnSpotLight"],
                    "validFrom": dictData["strValidFrom"],
                    "validUntil": dictData["strValidUntil"],
                    "discountedProducts": [
                        {
                            "sku": "EDA-42833",
                            "sellerDiscountPercentage": 9,
                            "totalDiscountPercentage": 10,
                            "discountPrice": "7775.78",
                            "listingName": "sunbeams-lifestyle-adjustable-dumbbell-steel-exercisefitnessgymworkout-equipment-1646963689542",
                            "discountTypeSku": dictData["strDiscountType"],
                            "discountNameSku": dictData["strName"],
                            "discountSpotlightSku": "On",
                            "isFeatured": True
                        },
                        {
                            "sku": "EDA-42834",
                            "sellerDiscountPercentage": 9,
                            "totalDiscountPercentage": 10,
                            "discountPrice": "13004.79",
                            "listingName": "sunbeams-lifestyle-adjustable-dumbbell-steel-workout-equipment-40-kg-1646963956219",
                            "discountTypeSku":dictData["strDiscountType"],
                            "discountNameSku": dictData["strName"],
                            "discountSpotlightSku": "On",
                            "isFeatured": True
                        }
                    ]
                }
            
            
    class sn:
        """SNS"""
        arrPUPayload = [{"sku":"EDA-43412","sellerDiscountPercentage":9,"totalDiscountPercentage":10},{"sku":"EDA-22090619","sellerDiscountPercentage":9,"totalDiscountPercentage":10}]
        
        def dictPDPayload(dictData):
            return {"name": dictData["strName"],
                    "discountType": dictData["strDiscountType"],
                    "isOnSpotlight": dictData["blnSpotLight"],
                    "validFrom": dictData["strValidFrom"],
                    "validUntil": dictData["strValidUntil"],
                    "discountedProducts": [
                        {
                            "sku": "EDA-43412",
                            "sellerDiscountPercentage": 9,
                            "totalDiscountPercentage": 10,
                            "discountPrice": "101.30",
                            "listingName": "ponds-bright-pore-conditioning-toner-with-niacinamide-and-sunscreen-100ml-1647841686300",
                            "discountTypeSku": dictData["strDiscountType"],
                            "discountNameSku": dictData["strName"],
                            "discountSpotlightSku": "On",
                            "isFeatured": True
                        },
                        {
                            "sku": "EDA-22090619",
                            "sellerDiscountPercentage": 9,
                            "totalDiscountPercentage": 10,
                            "discountPrice": "76.28",
                            "listingName": "human-nature-nourishing-facial-wash-50ml-1662433244037",
                            "discountTypeSku":dictData["strDiscountType"],
                            "discountNameSku": dictData["strName"],
                            "discountSpotlightSku": "On",
                            "isFeatured": True
                        }
                    ]
                }
            
          
          
          
          
            
class flashSale:
    """FLASH SALE"""
    arrPUPayload = [{"sku":"EDA-23081032","sellerDiscountPercentage":9,"totalDiscountPercentage":10},{"sku":"EDA-23081031","sellerDiscountPercentage":9,"totalDiscountPercentage":10}]
    
    def dictPDPayload(dictData):
        return {"isOnSpotlight": dictData["blnSpotLight"],
                "name": dictData["strName"],
                "validFrom": dictData["strValidFrom"],
                "validUntil": dictData["strValidUntil"],
                "discountedProducts": [
                    {
                        "sellerDiscountPercentage": 9,
                        "totalDiscountPercentage": 10,
                        "discountPrice": "2879.10",
                        "quantity": 1,
                        "sku": "EDA-23081032",
                        "isFeatured": True
                    },
                    {
                        "sellerDiscountPercentage": 9,
                        "totalDiscountPercentage": 10,
                        "discountPrice": "3239.10",
                        "quantity": 2,
                        "sku": "EDA-23081031",
                        "isFeatured": True
                    }
                ]
            }
    
    def dictCancelPayload(strUUID):
        return {"uuid":strUUID}





class products:
    """PRODUCTS"""
    def dictBlocked(strId):
        return {"status": "blocked",
                "_id": strId,
                "stepStatus": 1
            }
        
    def dictUnBlocked(strId):
        return {"status": "unblocked",
                "_id": strId,
                "stepStatus": 1
            }
    
    dictUnPublished = {"variantCombinations": [
                    {
                        "maxDiscountedProductType": {
                            "label": "Regular Price",
                            "typeName": "regular_price"
                        },
                        "childSkus": [],
                        "quantity": 189,
                        "wmsQuantity": 189,
                        "regularQuantity": 189,
                        "combinationName": "No Color",
                        "price": 1695,
                        "costPrice": 0,
                        "discount": 0,
                        "minStockQuantity": 0,
                        "sku": "EDA-44888",
                        "vendorSKU": "",
                        "sellingPrice": 1695,
                        "comboKeys": {
                            "color": "#######"
                        },
                        "productType": [],
                        "finalDiscountedPrice": 1695,
                        "type": "SIMPLE",
                        "_id": "6254ef7eebea4ca2c590da48",
                        "scheduledPricing": [],
                        "barcode": None
                    }
                ],
                "_id": "6254ef643a0aa4293e3f8e97",
                "stepStatus": 3,
                "isPublished": False
            }
        
    published = {"variantCombinations": [
                {
                    "combinationName": "No Color",
                    "childSkus": [],
                    "quantity": 189,
                    "scheduledPricing": [],
                    "price": 1695,
                    "costPrice": 0,
                    "wmsQuantity": 189,
                    "regularQuantity": 189,
                    "discount": 0,
                    "minStockQuantity": 0,
                    "sku": "EDA-44888",
                    "vendorSKU": "",
                    "sellingPrice": 1695,
                    "comboKeys": {
                        "color": "#######"
                    },
                    "productType": [],
                    "finalDiscountedPrice": 1695,
                    "maxDiscountedProductType": {
                        "label": "Regular Price",
                        "typeName": "regular_price"
                    },
                    "type": "SIMPLE",
                    "barcode": "EDA-44888",
                    "_id": "6254ef7eebea4ca2c590da48"
                }
            ],
            "_id": "6254ef643a0aa4293e3f8e97",
            "stepStatus": 4,
            "isPublished": True
        }
    
    
    updateBasicInformation = {"name": "xx Update Product xx",
                                "isFeatured": False,
                                "category": [
                                    {
                                        "_id": "5f5b916383aef5605833ab50",
                                        "name": "Bottle",
                                        "parentId": "5f5b916283aef5605833ab21",
                                        "icon": {
                                            "key": "icon"
                                        },
                                        "lName": "bowls-plates--utensils1599836515105",
                                        "ancestors": [
                                            {
                                                "_id": "5f5b916283aef5605833ab21",
                                                "name": "Bottles, Cups & Accessories"
                                            },
                                            {
                                                "_id": "5f5b916283aef5605833aae9",
                                                "name": "Feeding & Mealtime"
                                            }
                                        ]
                                    }
                                ],
                                "brand": {
                                    "_id": "5f33671c8cedc0010aeac01e",
                                    "name": "Tommee Tippee",
                                    "image": "https://edamama-bucket.s3.ap-southeast-1.amazonaws.com/source/00000001.png_1597204248917.png",
                                    "description": ""
                                },
                                "seller": {
                                    "_id": "5e49de2e6d4aef000953cfc1",
                                    "name": "MotherNurture",
                                    "image": "",
                                    "description": "",
                                    "isFeatured": False,
                                    "contactNumber": 9178627051,
                                    "email": "inventory@edamama.ph",
                                    "businessCategoryId": "5d492eecfc9fbc2d5c0c90b7"
                                },
                                "description": "<p>Finding easy solutions without compromising excellence, Tommee Tippee is created to champion parents like you! Tommee Tippee has been helping mamas and papas for more than 50 years. They create simple and intuitive products to make the roller coaster-like parenting easier! Helping you parent on— here’s Tommee Tippee.<br>Tommee Tippee CTN PP Bottle 5oz with Super Soft Slow Flow Teat (Pack of 2) is an award-winning Closer to Nature baby bottle, great for easy switching between breast and bottle feeding. With a guaranteed acceptance and built-in anti-colic valve, it’s super safe for your baby’s use! Plus, it has a soft silicone nipple and built-in valve. It’s BPA-free and has an award-winning design, and even recommended by 97% mamas!</p><figure class=\"image\"><img src=\"https://www.tommeetippee.com/media/product-support/Silicone-baby-bottle/Teat_Guide_1600x600.jpg\"></figure>",
                                "specifications": "<p>VOLUME: 5oz</p>",
                                "attribute": [
                                    {
                                        "_id": "5d4d079f7dd6930b4fb621e4",
                                        "name": "Party Planner"
                                    },
                                    {
                                        "_id": "5d4d07ac7dd6930b4fb621e5",
                                        "name": "Fashionista"
                                    },
                                    {
                                        "_id": "5d4d07be7dd6930b4fb621e6",
                                        "name": "Deal Queen"
                                    },
                                    {
                                        "_id": "5d4d07d87dd6930b4fb621e8",
                                        "name": "Modern Mama"
                                    },
                                    {
                                        "_id": "5d4d07e17dd6930b4fb621e9",
                                        "name": "Natural Mama"
                                    },
                                    {
                                        "_id": "5d51679ac9de875cff5fd192",
                                        "name": "Career Mama"
                                    },
                                    {
                                        "_id": "5d64cf966a9343160be40eca",
                                        "name": "Mamaste"
                                    },
                                    {
                                        "_id": "5d64cfb86a9343160be40ecb",
                                        "name": "Active Mama"
                                    },
                                    {
                                        "_id": "5d64d2496a9343160be40ecf",
                                        "name": "Mama Chef"
                                    },
                                    {
                                        "_id": "5d64d4e96a9343160be40ed1",
                                        "name": "Stay-At-Home Mama"
                                    },
                                    {
                                        "_id": "5d68ff336873573c15e5e721",
                                        "name": "Mama Teacher"
                                    },
                                    {
                                        "_id": "5d7f5aafab24383090d80ee4",
                                        "name": "Crafty Mama"
                                    },
                                    {
                                        "_id": "5d9320bfa7752c2eed9ac882",
                                        "name": "First-time Mama"
                                    },
                                    {
                                        "_id": "5f1072d9509459458a8cd814",
                                        "name": "Expecting Mama"
                                    },
                                    {
                                        "_id": "5f1072e47bf8752c5d3d99dd",
                                        "name": "Not a Mama"
                                    }
                                ],
                                "groupBying": False,
                                "isSubscribeSave": False,
                                "subscriptionDiscount": 0,
                                "productType": [],
                                "isMerchandise": False,
                                "videoUrl": "https://www.youtube.com/embed/AQrKn3EoiYE",
                                "shippingInfo": {
                                    "dimensions": "0 x 0 x 0",
                                    "weight": 0,
                                    "shippingPrice": 0,
                                    "isShippingPriceRequired": False
                                },
                                "deliveryOptions": [
                                    {
                                        "description": "",
                                        "isDescription": False,
                                        "isActive": False,
                                        "name": "30 Days Refundable",
                                        "imageName": "refundable",
                                        "type": 1,
                                        "key": "refundable"
                                    },
                                    {
                                        "description": "",
                                        "isDescription": False,
                                        "isActive": True,
                                        "name": "Cash on Delivery",
                                        "imageName": "cod",
                                        "type": 2,
                                        "key": "cod"
                                    },
                                    {
                                        "description": "",
                                        "isDescription": False,
                                        "isActive": False,
                                        "name": "Group Buy",
                                        "imageName": "group",
                                        "type": 3,
                                        "key": "group"
                                    },
                                    {
                                        "description": "",
                                        "isDescription": False,
                                        "isActive": False,
                                        "name": "Subscribe & Save",
                                        "imageName": "subscribe",
                                        "type": 4,
                                        "key": "subscribe"
                                    },
                                    {
                                        "description": "",
                                        "isDescription": True,
                                        "isActive": True,
                                        "name": "Express Delivery",
                                        "imageName": "expected",
                                        "type": 5,
                                        "key": "delivery"
                                    },
                                    {
                                        "description": "",
                                        "isDescription": True,
                                        "isActive": False,
                                        "name": "Warranty",
                                        "imageName": "warranty",
                                        "type": 6,
                                        "key": "warranty"
                                    }
                                ],
                                "skuType": "SIMPLE",
                                "stepStatus": 1,
                                "isRefundable": False,
                                "isCashOnDelivery": True,
                                "_id": "5f74334e38bd33494768d646",
                                "filters": [
                                    {
                                        "_id": "category",
                                        "displayType": "selectbox",
                                        "label": "Category",
                                        "name": "Category",
                                        "type": "multi",
                                        "options": [
                                            {
                                                "_id": "5f5b916383aef5605833ab50",
                                                "value": "Bottle",
                                                "parentInfo": {
                                                    "_id": "5f5b916283aef5605833aae9",
                                                    "title": "Feeding & Mealtime"
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        "_id": "brand",
                                        "displayType": "selectbox",
                                        "label": "Brand",
                                        "name": "Brand",
                                        "type": "single",
                                        "options": [
                                            {
                                                "_id": "5f33671c8cedc0010aeac01e",
                                                "value": "Tommee Tippee"
                                            }
                                        ]
                                    }
                                ]
                            }

    updateStockAndPrice = {"variantCombinations": [
                            {
                                "combinationName": "5oz,No Color",
                                "childSkus": [],
                                "quantity": 1000000,
                                "scheduledPricing": [],
                                "price": "1000",
                                "costPrice": 0,
                                "wmsQuantity": 1000000,
                                "regularQuantity": 1000000,
                                "discount": 0,
                                "minStockQuantity": 0,
                                "sku": "AAAA08742",
                                "vendorSKU": "",
                                "sellingPrice": "1000.00",
                                "comboKeys": {
                                    "Volume": "5oz",
                                    "color": "#######"
                                },
                                "productType": [],
                                "finalDiscountedPrice": 1000,
                                "maxDiscountedProductType": {
                                    "label": "Regular Price",
                                    "typeName": "regular_price"
                                },
                                "type": "SIMPLE",
                                "barcode": "5010415221001",
                                "_id": "5f743380b0ccb47047fb559a"
                            }
                        ],
                        "_id": "5f74334e38bd33494768d646",
                        "stepStatus": 3,
                        "isPublished": True
                    }

    updateAttributes = {"_id": "5f74334e38bd33494768d646",
                        "logisticsInfo": {
                            "productType": None,
                            "temperatureCondition": None,
                            "serialNumberManagement": True,
                            "vasManagement": None,
                            "shelfLifeManagementInfo": None
                        },
                        "manufacturePackageDimensionInfo": {
                            "length": None,
                            "width": None,
                            "height": None,
                            "weight": None
                        },
                        "stepStatus": 5
                    }
    
    revertBasicInformation = {"name": "CTN PP Bottle 5oz with Super Soft Slow Flow Teat (Pack of 2)",
                            "isFeatured": False,
                            "category": [
                                {
                                    "_id": "5f5b916383aef5605833ab50",
                                    "name": "Bottle",
                                    "parentId": "5f5b916283aef5605833ab21",
                                    "icon": {
                                        "key": "icon"
                                    },
                                    "lName": "bowls-plates--utensils1599836515105",
                                    "ancestors": [
                                        {
                                            "_id": "5f5b916283aef5605833ab21",
                                            "name": "Bottles, Cups & Accessories"
                                        },
                                        {
                                            "_id": "5f5b916283aef5605833aae9",
                                            "name": "Feeding & Mealtime"
                                        }
                                    ]
                                }
                            ],
                            "brand": {
                                "_id": "5f33671c8cedc0010aeac01e",
                                "name": "Tommee Tippee",
                                "image": "https://edamama-bucket.s3.ap-southeast-1.amazonaws.com/source/00000001.png_1597204248917.png",
                                "description": ""
                            },
                            "seller": {
                                "_id": "5e49de2e6d4aef000953cfc1",
                                "name": "MotherNurture",
                                "image": "",
                                "description": "",
                                "isFeatured": False,
                                "contactNumber": 9178627051,
                                "email": "inventory@edamama.ph",
                                "businessCategoryId": "5d492eecfc9fbc2d5c0c90b7"
                            },
                            "description": "<p>Finding easy solutions without compromising excellence, Tommee Tippee is created to champion parents like you! Tommee Tippee has been helping mamas and papas for more than 50 years. They create simple and intuitive products to make the roller coaster-like parenting easier! Helping you parent on— here’s Tommee Tippee.<br>Tommee Tippee CTN PP Bottle 5oz with Super Soft Slow Flow Teat (Pack of 2) is an award-winning Closer to Nature baby bottle, great for easy switching between breast and bottle feeding. With a guaranteed acceptance and built-in anti-colic valve, it’s super safe for your baby’s use! Plus, it has a soft silicone nipple and built-in valve. It’s BPA-free and has an award-winning design, and even recommended by 97% mamas!</p><figure class=\"image\"><img src=\"https://www.tommeetippee.com/media/product-support/Silicone-baby-bottle/Teat_Guide_1600x600.jpg\"></figure>",
                            "specifications": "<p>VOLUME: 5oz</p>",
                            "attribute": [
                                {
                                    "_id": "5d4d079f7dd6930b4fb621e4",
                                    "name": "Party Planner"
                                },
                                {
                                    "_id": "5d4d07ac7dd6930b4fb621e5",
                                    "name": "Fashionista"
                                },
                                {
                                    "_id": "5d4d07be7dd6930b4fb621e6",
                                    "name": "Deal Queen"
                                },
                                {
                                    "_id": "5d4d07d87dd6930b4fb621e8",
                                    "name": "Modern Mama"
                                },
                                {
                                    "_id": "5d4d07e17dd6930b4fb621e9",
                                    "name": "Natural Mama"
                                },
                                {
                                    "_id": "5d51679ac9de875cff5fd192",
                                    "name": "Career Mama"
                                },
                                {
                                    "_id": "5d64cf966a9343160be40eca",
                                    "name": "Mamaste"
                                },
                                {
                                    "_id": "5d64cfb86a9343160be40ecb",
                                    "name": "Active Mama"
                                },
                                {
                                    "_id": "5d64d2496a9343160be40ecf",
                                    "name": "Mama Chef"
                                },
                                {
                                    "_id": "5d64d4e96a9343160be40ed1",
                                    "name": "Stay-At-Home Mama"
                                },
                                {
                                    "_id": "5d68ff336873573c15e5e721",
                                    "name": "Mama Teacher"
                                },
                                {
                                    "_id": "5d7f5aafab24383090d80ee4",
                                    "name": "Crafty Mama"
                                },
                                {
                                    "_id": "5d9320bfa7752c2eed9ac882",
                                    "name": "First-time Mama"
                                },
                                {
                                    "_id": "5f1072d9509459458a8cd814",
                                    "name": "Expecting Mama"
                                },
                                {
                                    "_id": "5f1072e47bf8752c5d3d99dd",
                                    "name": "Not a Mama"
                                }
                            ],
                            "groupBying": False,
                            "isSubscribeSave": False,
                            "subscriptionDiscount": 0,
                            "productType": [],
                            "isMerchandise": False,
                            "videoUrl": "https://www.youtube.com/embed/AQrKn3EoiYE",
                            "shippingInfo": {
                                "dimensions": "0 x 0 x 0",
                                "weight": 0,
                                "shippingPrice": 0,
                                "isShippingPriceRequired": False
                            },
                            "deliveryOptions": [
                                {
                                    "description": "",
                                    "isDescription": False,
                                    "isActive": False,
                                    "name": "30 Days Refundable",
                                    "imageName": "refundable",
                                    "type": 1,
                                    "key": "refundable"
                                },
                                {
                                    "description": "",
                                    "isDescription": False,
                                    "isActive": True,
                                    "name": "Cash on Delivery",
                                    "imageName": "cod",
                                    "type": 2,
                                    "key": "cod"
                                },
                                {
                                    "description": "",
                                    "isDescription": False,
                                    "isActive": False,
                                    "name": "Group Buy",
                                    "imageName": "group",
                                    "type": 3,
                                    "key": "group"
                                },
                                {
                                    "description": "",
                                    "isDescription": False,
                                    "isActive": False,
                                    "name": "Subscribe & Save",
                                    "imageName": "subscribe",
                                    "type": 4,
                                    "key": "subscribe"
                                },
                                {
                                    "description": "",
                                    "isDescription": True,
                                    "isActive": True,
                                    "name": "Express Delivery",
                                    "imageName": "expected",
                                    "type": 5,
                                    "key": "delivery"
                                },
                                {
                                    "description": "",
                                    "isDescription": True,
                                    "isActive": False,
                                    "name": "Warranty",
                                    "imageName": "warranty",
                                    "type": 6,
                                    "key": "warranty"
                                }
                            ],
                            "skuType": "SIMPLE",
                            "stepStatus": 1,
                            "isRefundable": False,
                            "isCashOnDelivery": True,
                            "_id": "5f74334e38bd33494768d646",
                            "filters": [
                                {
                                    "_id": "category",
                                    "displayType": "selectbox",
                                    "label": "Category",
                                    "name": "Category",
                                    "type": "multi",
                                    "options": [
                                        {
                                            "_id": "5f5b916383aef5605833ab50",
                                            "value": "Bottle",
                                            "parentInfo": {
                                                "_id": "5f5b916283aef5605833aae9",
                                                "title": "Feeding & Mealtime"
                                            }
                                        }
                                    ]
                                },
                                {
                                    "_id": "brand",
                                    "displayType": "selectbox",
                                    "label": "Brand",
                                    "name": "Brand",
                                    "type": "single",
                                    "options": [
                                        {
                                            "_id": "5f33671c8cedc0010aeac01e",
                                            "value": "Tommee Tippee"
                                        }
                                    ]
                                }
                            ]
                        }
    
    revertStockAndPrice = {"variantCombinations": [
                            {
                                "combinationName": "5oz,No Color",
                                "childSkus": [],
                                "quantity": 1000000,
                                "scheduledPricing": [],
                                "price": "1000",
                                "costPrice": 0,
                                "wmsQuantity": 1000000,
                                "regularQuantity": 1000000,
                                "discount": 0,
                                "minStockQuantity": 0,
                                "sku": "AAAA08742",
                                "vendorSKU": "",
                                "sellingPrice": "800.00",
                                "comboKeys": {
                                    "Volume": "5oz",
                                    "color": "#######"
                                },
                                "productType": [],
                                "finalDiscountedPrice": 800,
                                "maxDiscountedProductType": {
                                    "label": "Regular Price",
                                    "typeName": "regular_price"
                                },
                                "type": "SIMPLE",
                                "barcode": "5010415221001",
                                "_id": "5f743380b0ccb47047fb559a"
                            }
                        ],
                        "_id": "5f74334e38bd33494768d646",
                        "stepStatus": 3,
                        "isPublished": True
                    }
    
    revertAttributes = {"_id": "5f74334e38bd33494768d646",
                        "logisticsInfo": {
                            "productType": None,
                            "temperatureCondition": None,
                            "serialNumberManagement": False,
                            "vasManagement": None,
                            "shelfLifeManagementInfo": None
                        },
                        "manufacturePackageDimensionInfo": {
                            "length": None,
                            "width": None,
                            "height": None,
                            "weight": None
                        },
                        "stepStatus": 5
                    }