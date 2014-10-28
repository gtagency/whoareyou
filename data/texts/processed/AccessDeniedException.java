public class AccessDeniedException extends Exception {
    private SecurityClearance requiredClearance;

    public AccessDeniedException(SecurityClearance req) {
        super("Must have " + req.name() + " to access.");
        requiredClearance = req;
    }

    public SecurityClearance getRequiredClearance() {
        return requiredClearance;
    }
}