package youngmin.api;

import com.google.gson.annotations.SerializedName;

public class MovieInfoJO
{
    @SerializedName("lastBuildDate")
    private String lastBuildDate;

    @SerializedName("total")
    private int total;

    @SerializedName("start")
    private int start;

    @SerializedName("display")
    private int display;

    @SerializedName("items")
    private ItemInfoJA[] items;

    public String getLastBuildDate() {
        return lastBuildDate;
    }

    public void setLastBuildDate(String lastBuildDate) {
        this.lastBuildDate = lastBuildDate;
    }

    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }

    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }

    public int getDisplay() {
        return display;
    }

    public void setDisplay(int display) {
        this.display = display;
    }

    public ItemInfoJA[] getItems() {
        return items;
    }

    public void setItems(ItemInfoJA[] items) {
        this.items = items;
    }

    public static class ItemInfoJA
    {
        @SerializedName("title")
        private String title;

        @SerializedName("link")
        private String link;

        @SerializedName("image")
        private String image;

        @SerializedName("subtitle")
        private String subtitle;

        @SerializedName("pubDate")
        private String pubDate;

        @SerializedName("director")
        private String director;

        @SerializedName("actor")
        private String actor;

        @SerializedName("userRating")
        private String userRating;

        public String getTitle() {
            return title;
        }

        public void setTitle(String title) {
            this.title = title;
        }

        public String getLink() {
            return link;
        }

        public void setLink(String link) {
            this.link = link;
        }

        public String getImage() {
            return image;
        }

        public void setImage(String image) {
            this.image = image;
        }

        public String getSubtitle() {
            return subtitle;
        }

        public void setSubtitle(String subtitle) {
            this.subtitle = subtitle;
        }

        public String getPubDate() {
            return pubDate;
        }

        public void setPubDate(String pubDate) {
            this.pubDate = pubDate;
        }

        public String getDirector() {
            return director;
        }

        public void setDirector(String director) {
            this.director = director;
        }

        public String getActor() {
            return actor;
        }

        public void setActor(String actor) {
            this.actor = actor;
        }

        public String getUserRating() {
            return userRating;
        }

        public void setUserRating(String userRating) {
            this.userRating = userRating;
        }
    }
}
