class com:
    """COMMON"""
    updateSubscriptionBtn = '(//button[text()=" Update Subscription "])[2]'
    skipOrderBtn = f'{updateSubscriptionBtn}/..//button[text()="Skip Order"]'
    skipAnOrderLbl = '//h1[text()="Skip an Order"]'
    yesSkipOrderBtn = '//button[text()="Yes, Skip Order"]'
    youveSkipOrderLbl = '//h1[text()=" You’ve Skipped an Order "]'
    yourNextOrderWillBeOnLbl = '//p[text()=" Your next order will be on "]'
    nextOrderDateLbl = f'{yourNextOrderWillBeOnLbl}/..//p[2]'
    gotItBtn = '//button[text()="GOT IT"]'
    changeProductBtn = f'{updateSubscriptionBtn}/../..//button[text()=" Change Product "]'
    cancelSubscriptionBtn = f'{updateSubscriptionBtn}/../..//button[text()=" Cancel Subscription "]'
    
    class cs:
        """CANCEL SUBSCRIPTION"""
        askForAssistancecBtn = '//button[text()="ASK FOR ASSISTANCE"]'
        
        
        





class at:
    """ACTIVE TAB"""
    productnameLbl  = '//span[@class="product-name"]'
    itemDisPriceLbl = '//span[@class="discounted-price"]'
    editSubscriptionBtn = '//button[text()=" Edit Subscription "]'
    deliversEveryLbl = '//div[@class="subscription-date"]/div[@class="d-none d-md-block"]'
    daysLbl  = '//div[@class="subscription-date"]/div[@class="d-none d-md-block"]/b'
    subscribeOnLbl = '//span[contains(text(),"Subscribed on")]'
    subscribeOnDateLbl = f'{subscribeOnLbl}/..//span[@class="date opaque"]'
    latestOrderPlacedLbl = '//span[contains(text(),"Latest Order Placed")]'
    latestOrderPlacedDateLbl = f'{latestOrderPlacedLbl}/..//span[@class="date"]'
    nextOrderLbl = '//span[contains(text(),"Next Order")]'
    nextOrderDateLbl = f'{nextOrderLbl}/..//span[@class="date-next"]'



 
 
class cp:
    """CHANGE PRODUCT"""
    changeProductLbl = '(//p[text()="Change Product"])[4]'
    
    class cp:
        """CHANGE PRODUCT"""
        oldProductNameLbl = '//div[@class="old field-value"]/span[@class="value"]'
        newProductNameLbl = '//div[@class="new field-value"]/span[@class="value"]'
        frequencyValueLbl = '//div[@class="frequency-dropdown"]//option[@selected="true"]'
        quantityLbl = '//p[text()="Quantity"]'
        quantityValueLbl = f'({quantityLbl}/..//span)[2]'
        discountedPriceLbl = '//p[@class="discounted-price"]'
        originalPriceLbl = '//p[@class="original-price ng-star-inserted"]'
        applyChangesBtn = '//button[text()=" Apply Changes "]'
        
    class us:
        """UPDATE SUBSCRIPTION"""
        updateSubscriptionLbl = '//h2[text()="Update Subscription"]'
        oldProductNameLbl = '(//div[@class="old-wrapper field-value"]/span)[1]'
        oldProductPriceLbl = '(//div[@class="old-wrapper field-value"]/span)[3]'
        newProductNameLbl = f'({updateSubscriptionLbl}/../..//div[@class="new field-value"]/span[@class="value"])[1]'
        newProductPriceLbl = f'({updateSubscriptionLbl}/../..//div[@class="new field-value"]/span[@class="value"])[2]'
        applyChangesBtn = '//button[text()="Apply Changes"]'





class st:
    """SUBMIT TICKET"""
    submitATicketLbl = '//h2[text()="Submit a ticket"]'