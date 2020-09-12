package youngmin.login;

public class LoginBean
{
    private String userId;
    private String userPw;

    final String _userId = "youngmin";
    final String _userPw = "1234";

    public String getUserId() {
        return userId;
    }

    public String getUserPw() {
        return userPw;
    }

    public void setUserPw(String userPw) {
        this.userPw = userPw;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public boolean checkUser()
    {
        if (userId.equals(_userId) && userPw.equals(_userPw))
            return true;
        else
            return false;
    }
}
