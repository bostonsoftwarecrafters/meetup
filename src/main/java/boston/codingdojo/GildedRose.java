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

    public void updateQuality() {
        for (int i = 0; i < items.length; i++) {
            updateItemQuality(items[i]);
        }
    }

    private void updateBackstagePasses(Item item) {

        if (item.quality < MAX_STANDARD_QUALITY) {
            item.quality = item.quality + 1;


            if (item.daysToExpire < 11) {
                if (item.quality < MAX_STANDARD_QUALITY) {
                    item.quality = item.quality + 1;
                }
            }

            if (item.daysToExpire < 6) {
                if (item.quality < MAX_STANDARD_QUALITY) {
                    item.quality = item.quality + 1;
                }
            }
        }


    }

    private void updateItemQuality(Item item) {

        if (item.name.equals(PRODUCT_BACKSTAGE_PASSES)) {
            updateBackstagePasses(item);
//        }else if(){

            if (!(item.name.equals(PRODUCT_AGED_BRIE)
                    || item.name.equals(PRODUCT_BACKSTAGE_PASSES) || item.name.equals(PRODUCT_SULFURAS))) {


                if (item.quality > MIN_STANDARD_QUALITY) {
//                if (!item.name.equals(PRODUCT_SULFURAS)) {
                    item.quality = item.quality - 1;
//                }
                }
            }
            if(item.name.equals(PRODUCT_AGED_BRIE)){
                if (item.quality < MAX_STANDARD_QUALITY) {
                    item.quality = item.quality + 1;

//                if (item.name.equals(PRODUCT_BACKSTAGE_PASSES)){
//                updateBackstagePasses(item);
//
//                }
                }
            }
//            else {
//                if (item.quality < MAX_STANDARD_QUALITY) {
//                    item.quality = item.quality + 1;
//
////                if (item.name.equals(PRODUCT_BACKSTAGE_PASSES)){
////                updateBackstagePasses(item);
////
////                }
//                }
//            }

            if (!item.name.equals(PRODUCT_SULFURAS)) {
                item.daysToExpire = item.daysToExpire - 1;
            }

            if (item.daysToExpire < 0) {
                if (!item.name.equals(PRODUCT_AGED_BRIE)) {
                    if (!item.name.equals(PRODUCT_BACKSTAGE_PASSES)) {
                        if (item.quality > MIN_STANDARD_QUALITY) {
                            if (!item.name.equals(PRODUCT_SULFURAS)) {
                                item.quality = item.quality - 1;
                            }
                        }
                    } else {
                        item.quality = item.quality - item.quality;
                    }
                } else {
                    if (item.quality < MAX_STANDARD_QUALITY) {
                        item.quality = item.quality + 1;
                    }
                }
            }
        }
    }
}