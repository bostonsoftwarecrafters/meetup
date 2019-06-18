package boston.codingdojo;

/** assumption: product owner doesn't believe quality can start out over 50 */

class GildedRose {
	// TODO Convert tests to parameterized test
	// TODO Use constants in updateQuality

	Item[] items;




	public static final String PRODUCT_EXAMPLE_NORMAL_ITEM = "Example Normal Item";
    public static final String PRODUCT_BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert";
	public static final String PRODUCT_AGED_BRIE = "Aged Brie";
	public static final String PRODUCT_SULFURAS = "Sulfuras, Hand of Ragnaros";
	public static final int MIN_STANDARD_QUALITY = 0;
	public static final int MAX_STANDARD_QUALITY = 50;
	public static final int NORMAL_ITEM_DEFAULT_DELTA_QUALITY = -1;
	public static final int NORMAL_ITEM_EXPIRED_DELTA_QUALITY = 2 * NORMAL_ITEM_DEFAULT_DELTA_QUALITY;
	public static final int AGED_BRIE_DEFAULT_DELTA_QUALITY = 1;
	public static final int AGED_BRIE_EXPIRED_DELTA_QUALITY = AGED_BRIE_DEFAULT_DELTA_QUALITY * 2;
	public static final int DEFAULT_DELTA_SELL_IN = -1;
	public static final int SELL_IN_EXPIRATION = 0;





    public GildedRose(Item[] items) {
        this.items = items;
    }

    public void unRefactoredUpdate() {
        for (int i = 0; i < items.length; i++) {
            Item currentItem = items[i];
            updateItem(currentItem);
        }
    }

    private void updateItem(Item currentItem) {
        if (PRODUCT_SULFURAS.equals(currentItem.name)) {
           return;
        }

        if (!currentItem.name.equals(PRODUCT_AGED_BRIE)
                && !currentItem.name.equals(PRODUCT_BACKSTAGE_PASSES)) {
            if (currentItem.quality > MIN_STANDARD_QUALITY) {
                if (!currentItem.name.equals(PRODUCT_SULFURAS)) {
                    currentItem.quality = currentItem.quality - 1;
                }
            }
        } else {
            if (currentItem.quality < MAX_STANDARD_QUALITY) {
                currentItem.quality = currentItem.quality + 1;

                if (currentItem.name.equals(PRODUCT_BACKSTAGE_PASSES)) {
                    if (currentItem.daysToExpire < 11) {
                        if (currentItem.quality < MAX_STANDARD_QUALITY) {
                            currentItem.quality = currentItem.quality + 1;
                        }
                    }

                    if (currentItem.daysToExpire < 6) {
                        if (currentItem.quality < MAX_STANDARD_QUALITY) {
                            currentItem.quality = currentItem.quality + 1;
                        }
                    }
                }
            }
        }

        if (!currentItem.name.equals(PRODUCT_SULFURAS)) {
            currentItem.daysToExpire = currentItem.daysToExpire - 1;
        }

        if (currentItem.daysToExpire < 0) {
            if (!currentItem.name.equals(PRODUCT_AGED_BRIE)) {
                if (!currentItem.name.equals(PRODUCT_BACKSTAGE_PASSES)) {
                    if (currentItem.quality > MIN_STANDARD_QUALITY) {
                        if (!currentItem.name.equals(PRODUCT_SULFURAS)) {
                            currentItem.quality = currentItem.quality - 1;
                        }
                    }
                } else {
                    currentItem.quality = currentItem.quality - currentItem.quality;
                }
            } else {
                if (currentItem.quality < MAX_STANDARD_QUALITY) {
                    currentItem.quality = currentItem.quality + 1;
                }
            }
        }
    }

    public void updateQuality() {
        for (int i = 0; i < items.length; i++) {
            if (!items[i].name.equals(PRODUCT_AGED_BRIE)
                    && !items[i].name.equals(PRODUCT_BACKSTAGE_PASSES)) {
                if (items[i].quality > MIN_STANDARD_QUALITY) {
                    if (!items[i].name.equals(PRODUCT_SULFURAS)) {
                        items[i].quality = items[i].quality - 1;
                    }
                }
            } else {
                if (items[i].quality < MAX_STANDARD_QUALITY) {
                    items[i].quality = items[i].quality + 1;

                    if (items[i].name.equals(PRODUCT_BACKSTAGE_PASSES)) {
                        if (items[i].daysToExpire < 11) {
                            if (items[i].quality < MAX_STANDARD_QUALITY) {
                                items[i].quality = items[i].quality + 1;
                            }
                        }

                        if (items[i].daysToExpire < 6) {
                            if (items[i].quality < MAX_STANDARD_QUALITY) {
                                items[i].quality = items[i].quality + 1;
                            }
                        }
                    }
                }
            }

            if (!items[i].name.equals(PRODUCT_SULFURAS)) {
                items[i].daysToExpire = items[i].daysToExpire - 1;
            }

            if (items[i].daysToExpire < 0) {
                if (!items[i].name.equals(PRODUCT_AGED_BRIE)) {
                    if (!items[i].name.equals(PRODUCT_BACKSTAGE_PASSES)) {
                        if (items[i].quality > MIN_STANDARD_QUALITY) {
                            if (!items[i].name.equals(PRODUCT_SULFURAS)) {
                                items[i].quality = items[i].quality - 1;
                            }
                        }
                    } else {
                        items[i].quality = items[i].quality - items[i].quality;
                    }
                } else {
                    if (items[i].quality < MAX_STANDARD_QUALITY) {
                        items[i].quality = items[i].quality + 1;
                    }
                }
            }
        }
    }
}