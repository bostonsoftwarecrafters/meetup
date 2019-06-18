package boston.codingdojo;

import boston.codingdojo.GildedRose;
import boston.codingdojo.Item;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

import java.util.Arrays;

import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

@RunWith(Parameterized.class)
public class ParameterizedItemTest {

	private GildedRose inn;

	private String testDescription;
	private String product;
	private int initialDaysToExpire;
	private int initialQuality;
	private int expectedDaysToExpire;
	private int expectedQuality;

//TODO Copy tests from other product types into our data array
	
	@Parameters(name="{index}: {0}")
	public static Iterable<Object[]> data() {
		return(Arrays.asList(new Object[][] {
			// description, product, initial daysToExpire, initial quality, expected daysToExpire, expected quality
                {"Normal item degrades when not expired",   "foo", 5,  4, 7, 6},
                {"Normal item quality does not degrade when quality zero", "foo", 4, 3, 0, 0},
                {"Normal item degrades double when expire = 0",      "foo", 0,  -1, 7, 5},
                {"Normal item degrades double when expire < 0", "foo", -1, -2, 7, 5},
                {"Sulfuras quality does not change", GildedRose.PRODUCT_SULFURAS, 3, 3, 80, 80},
                {"Sulfuras quality does not change when expire", GildedRose.PRODUCT_SULFURAS, -1, -1, 80, 80},
                {"AgedBrie quality caps at 50", GildedRose. PRODUCT_AGED_BRIE, 2, 1, 50, 50},
                {"AgedBrie quality caps at 50 when expire", GildedRose. PRODUCT_AGED_BRIE, 0, -1, 50, 50},
                {"AgedBrie quality caps at 50 when expire", GildedRose. PRODUCT_AGED_BRIE, -1, -2, 50, 50},
                {"AgedBrie quality caps at 50 when expire", GildedRose. PRODUCT_AGED_BRIE, 0, -1, 49, 50},
                {"AgedBrie quality +1", GildedRose. PRODUCT_AGED_BRIE, 5, 4, 7, 8},
                {"AgedBrie quality +1", GildedRose. PRODUCT_AGED_BRIE, 1, 0, 7, 8},
                {"AgedBrie quality +2 when expire", GildedRose. PRODUCT_AGED_BRIE, 0, -1, 41, 43},
                {"AgedBrie quality +2 when expire", GildedRose. PRODUCT_AGED_BRIE, -2, -3, 46, 48},

        }));
	}
	
	public ParameterizedItemTest(
			String testDescription,
			String product,
			int initialDaysToExpire,
			int expectedDaysToExpire,
			int initialQuality,
			int expectedQuality )
	{
		this.testDescription = testDescription;
		this.product = product;
		this.initialDaysToExpire = initialDaysToExpire;
		this.initialQuality = initialQuality;
		this.expectedDaysToExpire = expectedDaysToExpire;
		this.expectedQuality = expectedQuality;
	}

	@Test
	public void parameterizedItemTest() {
		Item[] items = {new Item(product,initialDaysToExpire,initialQuality)};
		inn = new GildedRose(items);
		Item item = items[0];
		inn.updateQuality();
		assertEquals(expectedQuality, item.quality);
		assertEquals(expectedDaysToExpire, item.daysToExpire);
	}


   


}
