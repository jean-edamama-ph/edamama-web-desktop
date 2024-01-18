class com:
    """COMMON"""
    savedItemsLbl = '//div[text()="Saved Items"]'
    searchBtn = '//button//span[contains(text(),"Search")]'
    searchTxt = '//input[@data-placeholder="Search Items by title"]'
    noWishlistLbl = '//div[text()="Currently no wishlist found"]'
    confirmationDialogLbl = '//h1[text()="Confirmation"]'
    confirmationDialogYesBtn = '//button//span[normalize-space(text())="Yes"]'
    confirmationDialogNoBtn = '//button//span[normalize-space(text())="No"]'
    loadingSpinnerImg = '//mat-spinner[@role="progressbar"]'
    def itemHeartBtn(strItemName):
        return f'//span[normalize-space(text())="{strItemName}"]/../..//mat-icon[@data-mat-icon-name="heart_wishlist_clicked"]'
    def itemBrandLbl(strItemName):
        return f'//span[normalize-space(text())="{strItemName}"]/../span[@class="brand_name"]'
    def itemNameLbl(strItemName):
        return f'//span[normalize-space(text())="{strItemName}"]'
    def itemSaleLbl(strItemName):
        return f'//span[normalize-space(text())="{strItemName}"]/..//span[@class="sale-off ng-star-inserted"]'
    def itemOriginalPriceLbl(strItemName):
        return f'//span[normalize-space(text())="{strItemName}"]/..//span[@class="original-price ng-star-inserted"]'
    def itemDiscountedPriceLbl(strItemName):
        return f'//span[normalize-space(text())="{strItemName}"]/..//span[@class="discounted-price"]'
    def itemImg(strItemName):
        return f'//span[normalize-space(text())="{strItemName}"]/../..//img'