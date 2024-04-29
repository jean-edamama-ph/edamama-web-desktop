class com:
    """COMMON"""
    plpStatusLbl = '//p[@class="rf-product-list-page-status-text ng-star-inserted"]'
    colorSectionPnl = '//section[@class="rf-product-filter -color ng-star-inserted"]'
    ageGroupSectionPnl = '//section[@class="rf-product-filter -age-group ng-star-inserted"]'
    genderSectionPnl = '//section[@class="rf-product-filter -gender ng-star-inserted"]'
    brandSectionPnl = '//section[@class="rf-product-filter -brand -no-border ng-star-inserted"]'
    priceFilterSectionPnl = '//section[@class="rf-product-filter no-gutters -price ng-star-inserted"]'
    sortByLbl = '//span[text()="Sort By"]'
    relevanceBtn = '//span[contains(text(), "Relevance")]'
    shopDrawerPnl = '//div[contains(text(), "Shop")]/../../div[contains(@class, "index-hit")]'
    discoverDrawerPnl = '//div[contains(text(), "Discover")]/../../div[contains(@class, "index-hit")]'
    recentSearchesLbl = '//h2[contains(text(), "Recent Searches")]'
    def recentSearchLbl(strValue):
        return f'{com.recentSearchesLbl}/../..//ul/li/span[contains(text(), "{strValue}")]'
    def recentSearchSequenceLbl(intCtr):
        return f'{com.recentSearchesLbl}/../..//ul/li[{intCtr}]'


class flt:
    """FILTERS"""
    priceHeaderLbl = '//h3[contains(text(),"Price")]'
    minPriceLbl = '//span[text()="Min Price"]'
    maxPriceLbl = '//span[text()="Max Price"]'
    minPesoSignLbl = f'{minPriceLbl}/../div/span[contains (text(),"₱")]'
    maxPesoSignLbl = f'{maxPriceLbl}/../div/span[contains (text(),"₱")]'
    minPriceTxt = '//input[@id="minPrice"]'
    maxPriceTxt = '//input[@id="maxPrice"]'
    applyBtn = '//span[contains(text(), "Apply")]'
    colorHeaderLbl = '//h3[contains(text(), "Color")]'    
    ageGrpHeaderLbl = '//h3[contains(text(),"Age Group")]'
    genderHeaderLbl = '//h3[contains(text(),"Gender")]'
    brandHeaderLbl = '//h3[contains(text(),"Gender")]'
    