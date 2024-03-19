class pl:
    """Product Listing Filter"""
    tickedSSProdSpotlightChk = '//h3[text()="Product Spotlight"]/..//li[3]/mat-checkbox[@class="mat-checkbox mat-primary mat-checkbox-checked"]'
    def sNSBadgeHeader(strValue):
        return f'//span[contains(text(), "{strValue}")]/../../../..//div/div[contains(text(), "Subscribe & Save")]'
    def prodCardImg(strValue):
        return f'//img[contains(@alt, "{strValue}")]'
    