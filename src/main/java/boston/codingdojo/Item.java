package boston.codingdojo;

public class Item {

	public String name;

    public int daysToExpire;

    public int quality;

    public Item (){
    	
    }
    public Item(String name, int daysToExpire, int quality) {
        this.name = name;
        this.daysToExpire = daysToExpire;
        this.quality = quality;
    }

   @Override
   public String toString() {
        return this.name + ", " + this.daysToExpire + ", " + this.quality;
    }
}
