package boston.codingdojo;

import junit.framework.Assert;
import org.junit.Test;

/**
 * @author Danil Suits (danil@vast.com)
 */
public class OracleTest {
    void compareToOracle(String item, int sellin, int quality) {
        Item[] expected = new Item[1];
        Item[] actual = new Item[1];
        expected[0] = new Item(item, sellin, quality);
        actual[0] = new Item(item, sellin, quality);
        {
            GildedRose inn = new GildedRose(expected);
            inn.updateQuality();
        }
        {
            GildedRose inn = new GildedRose(actual);
            inn.unRefactoredUpdate();
        }

        Assert.assertEquals("Quality", expected[0].quality, actual[0].quality);
        Assert.assertEquals("Days to Expire", expected[0].daysToExpire, actual[0].daysToExpire);
        Assert.assertEquals("Name", expected[0].name, actual[0].name);
    }

    @Test
    public void test1() {
        compareToOracle(GildedRose.PRODUCT_BACKSTAGE_PASSES, 10, 0);
    }
}
