public enum SecurityClearance {
    NONE, CONFIDENTIAL, SECRET, TOP_SECRET;

    public String toString() {
        return name().substring(0, 1) + name().substring(1).toLowerCase();
    }
};