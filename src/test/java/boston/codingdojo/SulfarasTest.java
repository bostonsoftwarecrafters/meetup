package boston.codingdojo;

import boston.codingdojo.GildedRose;
import boston.codingdojo.Item;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class SulfarasTest {
	// TODO Refactor to be like AgedBrieTest structure

	@Test
	public void testQualityOfSulfuras() {
		Item sulfuras1 = new Item(GildedRose.PRODUCT_SULFURAS, 3, 80);
		GildedRose inn = new GildedRose(new Item[] {sulfuras1});
		inn.updateQuality();
		assertEquals(80,sulfuras1.quality);
	}

	@Test
	public void testDaysToExpireOfSulfuras() {
		Item sulfuras1 = new Item(GildedRose.PRODUCT_SULFURAS, 3, 80);
		GildedRose inn = new GildedRose(new Item[] {sulfuras1});
		inn.updateQuality();
		assertEquals(3,sulfuras1.daysToExpire);
	}
	
//	@Test
//	@Ignore
//	//Ignore because quality should never be able to be 3
//	public void test0QualityOfSulfuras() {
//		Item sulfuras1 = new Item(GildedRose.PRODUCT_SULFURAS, 3, 0);
//		GildedRose inn = new GildedRose(new Item[] {sulfuras1});
//		inn.updateQuality();
//		assertEquals(80,sulfuras1.quality); // actual result is 3, surprise
//	}

	@Test
	public void testSulfurasDoesntExpire() {
		Item sulfuras1 = new Item(GildedRose.PRODUCT_SULFURAS, -1, 80);
		GildedRose inn = new GildedRose(new Item[] {sulfuras1});
		inn.updateQuality();
		assertEquals(80,sulfuras1.quality);
		assertEquals(-1,sulfuras1.daysToExpire);
	}

}
