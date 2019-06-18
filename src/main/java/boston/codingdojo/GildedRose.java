package boston.codingdojo;

import java.util.Arrays;
import java.util.List;

import static java.lang.Math.max;
import static java.lang.Math.min;

/**
 * assumption: product owner doesn't believe quality can start out over 50
 */

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

    public void updateQuality() {
        for (int i = 0; i < items.length; i++) {

            Item currentItem = items[i];

            if (currentItem.name.equals(PRODUCT_SULFURAS)) {
                continue;
            }

            if (isBasicItem(currentItem)) {
                currentItem.quality = currentItem.quality - 1;
            } else {
                changeQualityOfNonBasics(currentItem);
            }

            if (!currentItem.name.equals(PRODUCT_SULFURAS)) {
                currentItem.daysToExpire = currentItem.daysToExpire - 1;
            }

            if (currentItem.daysToExpire < 0) {
                if (isBasicItem(currentItem)) {
                    currentItem.quality = currentItem.quality - 1;
                } else {
                    currentItem.quality = currentItem.quality + 1;
                }
                if (currentItem.name.equals(PRODUCT_BACKSTAGE_PASSES)) {
                    currentItem.quality = 0;
                }
            }

            currentItem.quality = min(currentItem.quality, MAX_STANDARD_QUALITY);
            currentItem.quality = max(currentItem.quality, MIN_STANDARD_QUALITY);
        }
    }

    private void changeQualityOfNonBasics(Item currentItem) {


        int specialItemDelta = 1;

        if (currentItem.name.equals(PRODUCT_BACKSTAGE_PASSES)) {
            if (currentItem.daysToExpire < 6) {
                specialItemDelta = 3;
            } else if (currentItem.daysToExpire < 11) {
                specialItemDelta = 2;
            }
        }
        currentItem.quality = currentItem.quality + specialItemDelta;
    }

    private boolean isBasicItem(Item item) {
        String[] nonBasic = {PRODUCT_AGED_BRIE, PRODUCT_BACKSTAGE_PASSES, PRODUCT_SULFURAS};
        List<String> nonBasicList = Arrays.asList(nonBasic);
        return !nonBasicList.contains(item.name);
    }
}