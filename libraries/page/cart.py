class com:
    """COMMON"""
    yourBagsEmptyLbl = '//p[contains(text(),"Your cart\'s")][text()=" looking empty right now. "]'
    yourBagsEmptyDescLbl = '//p[contains(text(),"But that\'s okay! Exciting offers are waiting for you. Start browsing the shop and get the best deals for you.")]'
    startBrowsingBtn = '//button[contains(text(),"Start Browsing")]'

class mc:
    """MY CART"""
    myBagLbl = '//p[text()="My Cart"]'
    youHaveXProductLbl = '//p[starts-with(text()," You have")][text()="product"][text()=" in your cart. "]'
    itemSmallPicImg = '//div[@class="img-wrapper"]/img'
    itemBrandLbl = '//div[@class="cart-items"]//span[@class="brand"]'
    itemNameLbl = '//span[@class="name"]'
    heartIconBtn = '//mat-icon[text()="favorite_border"]'
    deleteIconBtn = '(//img[@src="assets/images/cart/icons/bin-glyph.png"])[1]'
    colorLbl = '//p[@class="variant"]'
    giftWrapChk = '//span[@class="mat-checkbox-frame"]'
    giftWrapLbl = '//span[contains(text(),"Giftwrap")]'
    quantityMinusIconBtn = '//button//mat-icon[text()="remove"]'
    quantityOutputLbl = '//span[@class="qty-counter"] | //mat-select[contains(@class,"subscription-qty")]//span[contains(@class,"mat-select-min-line")]'
    quantityPlusIconBtn = '//button//mat-icon[text()="add"]'
    itemPriceLbl = '//p[@class="default-price"]'
    itemDiscountTagLbl = '//p[@class="discount-tag"]'
    itemDiscountedPrice = '//p[@class="default-price"]/..//p[@class="discounted-price"]'
    
class od:
    """ORDER DETAILS"""
    giftWrapBannerImg = '//button[@class="gift-wrapping-banner ng-star-inserted"][text() = " Free Gift Wrap "]'
    orderDetailsLbl = '//p[text()="Order Details"]'
    subTotalLbl = '//p[text()="Subtotal"]'
    subTotalAmountLbl = '//p[text()="Subtotal"]/../p[@class="value"]'
    giftWrapLbl = '//p[text()="Gift Wrap"]'
    giftWrapAmountLbl = '//p[text()="Gift Wrap"]/../p[@class="value"]'
    shippingLbl = '//p[text()="Shipping"]'
    shippingAmountLbl = '//span[contains(@class,"value -calculate")]'
    totalLbl = '//p[text()="Total"]'
    totalAmountLbl = '//p[text()="Total"]/../p[@class="value"]'
    weWillProvideAnUpdateLbl = '//p[contains(text(),"*We will provide an updated total at the checkout once you’ve entered a delivery address.")]'
    checkOutBtn = '//button[normalize-space(text())="Checkout"][@class="checkout-btn"]'
    
class cm:
    """CONFIRMATION MESSAGE"""
    confirmationLbl = '//h1[text()="Confirmation"]'
    confirmationMsg = '//p[text()="Are you sure you want to delete this product from your cart?"]'
    noBtn = '//button/span[contains(text(),"No")]'
    yesBtn = '//button/span[contains(text(),"Yes")]'