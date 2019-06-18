package boston.codingdojo;

import boston.codingdojo.GildedRose;
import boston.codingdojo.Item;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class AgedBrieTest {
	


	private GildedRose inn;

	/**
	 * @param daysToExpire
	 * @param quality
	 * @return
	 */
	

	@Test
	public void testAgedBrieIncrements() {
		int daysToExpire = 5;
		int quality = 7;
		int expectedQuality = 8;
		Item item = createInnWithStandardAgedBrie(daysToExpire, quality);
		inn.updateQuality();
		assertEquals(expectedQuality, item.quality);
		System.out.format("%s Quality => %s %s%n",daysToExpire,quality,expectedQuality);
	}


	@Test
	public void testAgedBrieDaysToExpireDecrements() {
		int daysToExpire = 5;
		int quality = 7;
		int expectedDaysToExpire = daysToExpire + GildedRose.DEFAULT_DELTA_SELL_IN;
		Item item = createInnWithStandardAgedBrie(daysToExpire, quality);
		inn.updateQuality();
		assertEquals(expectedDaysToExpire, item.daysToExpire);
	}
	
	@Test
	public void testAgedBrieQualityCapsAt50() {
		int daysToExpire = 5;
		int quality = GildedRose.MAX_STANDARD_QUALITY;
		int expectedQuality = quality;
		Item item = createInnWithStandardAgedBrie(daysToExpire, quality);
		inn.updateQuality();
		assertEquals(expectedQuality, item.quality);
		System.out.format("%s Quality => %s %s%n",daysToExpire,quality,expectedQuality);
	}
	
	@Test
	public void testAgedBrieQualityStableAfterDaysToExpireAt50() {
		int daysToExpire = GildedRose.SELL_IN_EXPIRATION;
		int quality = GildedRose.MAX_STANDARD_QUALITY;
		Item item = createInnWithStandardAgedBrie(daysToExpire, quality);
		inn.updateQuality();
		assertEquals(quality, item.quality);
		System.out.format("%s Quality => %s %s%n",daysToExpire,quality,quality);
	}
	
	private Item createInnWithStandardAgedBrie(int daysToExpire, int quality) {
		Item[] items = {new Item(GildedRose.PRODUCT_AGED_BRIE,daysToExpire,quality)};
		inn = new GildedRose(items);
		return items[0];
	}

	@Test
	public void testAgedBrieQualityIncreasesByTwoAfterDaysToExpireUnder50() {
		int daysToExpire = GildedRose.SELL_IN_EXPIRATION;
		int quality = 46;
		int expectedQuality = quality + GildedRose.AGED_BRIE_EXPIRED_DELTA_QUALITY;
		Item item = createInnWithStandardAgedBrie(daysToExpire, quality);
		inn.updateQuality();
		assertEquals(expectedQuality, item.quality);
		System.out.format("%s Quality => %s %s",daysToExpire,quality,expectedQuality);
	}
}
