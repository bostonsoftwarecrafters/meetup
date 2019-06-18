package boston.codingdojo;

import org.junit.Assert;
import org.junit.Test;

/**
 * @author Danil Suits (danil@vast.com)
 */
public class BackStagePassTest {
    @Test
    public void afterConcert (){
       Assert.assertEquals(0, age_backstagePass(0, 10));
    }

    @Test
    public void sellinGreaterThanTen () {
        final int inputQuality = 12;
        Assert.assertEquals(inputQuality + 1, age_backstagePass(15, inputQuality));
    }

    @Test
    public void sellinBetweenFiveAndTen () {
        final int expectedQuality = 13;
        Assert.assertEquals(expectedQuality, age_backstagePass(7, 11));
    }

    @Test
    public void lessThanFive () {
        final int expectedQuality = 13;
        Assert.assertEquals(expectedQuality, age_backstagePass(3, 10));
    }

    @Test
    public void sellInAtFive () {
        final int expectedQuality = 13;
        Assert.assertEquals(expectedQuality, age_backstagePass(5, 10));
    }

    @Test
    public void sellInAtTen () {
        final int expectedQuality = 13;
        Assert.assertEquals(expectedQuality, age_backstagePass(10, 11));
    }

    @Test
    public void alwaysLessThanFifty () {
        final int expectedQuality = 50;
        Assert.assertEquals(expectedQuality, age_backstagePass(15, 50));
    }

    @Test
    public void qualityDoesnotChange() {
        int whateverqualityweregoingtosendit = 20;
        Assert.assertEquals(whateverqualityweregoingtosendit, new Item(GildedRose.PRODUCT_BACKSTAGE_PASSES, 7, whateverqualityweregoingtosendit).quality );
    }


    int age_backstagePass(int sellIn, int quality) {
        Item[] items = new Item[1];
        GildedRose inn = new GildedRose(items);

        items[0] = new Item(GildedRose.PRODUCT_BACKSTAGE_PASSES, sellIn, quality);

        inn.updateQuality();
        return items[0].quality;
    }

}
