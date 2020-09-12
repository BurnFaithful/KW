package youngmin.login;

import java.sql.*;

public class UserDAO {

    private Connection conn = null;
    private PreparedStatement pstmt = null;
    private ResultSet rs = null;

    public UserDAO()
    {
        String url = "jdbc:mysql://localhost:3306/kw";
        String dbID = "root";
        String dbPW = "cout49!";

        try
        {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection(url, dbID, dbPW);
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }

    public int login(String id, String pw) {
        String query = "SELECT userPW FROM USER WHERE userID = ?";

        try
        {
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, id);

            rs = pstmt.executeQuery();
            if (rs.next())
            {
                if (rs.getString(1).equals(pw))
                {
                    return 1; // 로그인 성공
                }
                return 0; // 비밀번호 틀림
            }
            return -1; // 일치 ID 없음
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }
        }
        return -2; // DB 접속 오류
    }

    public int join(UserDTO user) {
        String query = "INSERT INTO USER VALUES (?, ?, ?, ?, ?, ?, ?)";
        try
        {
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, user.getUserID());
            pstmt.setString(2, user.getUserPW());
            pstmt.setString(3, user.getUserName());
            pstmt.setString(4, user.getUserNickname());
            pstmt.setString(5, user.getPhoneNumber());
            pstmt.setString(6, user.getUserMail());
            pstmt.setString(7, user.getSex());
            return pstmt.executeUpdate();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally {
            try
            {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }
        }

        return -1;
    }

    public UserDTO getUserInfo(String id)
    {
        String query = "SELECT userName, userNickname, phoneNumber, userMail, sex FROM USER WHERE userID = ?";

        try
        {
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, id);
            rs = pstmt.executeQuery();
            if (rs.next())
            {
                UserDTO user = new UserDTO();
                user.setUserID(id);
                user.setUserName(rs.getString(1));
                user.setUserNickname(rs.getString(2));
                user.setPhoneNumber(rs.getString(3));
                user.setUserMail(rs.getString(4));
                user.setSex(rs.getString(5));
                return user;
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally {
            try
            {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }
        }

        return null;
    }

    public int update(UserDTO user)
    {
        String query = "UPDATE USER SET userName = ?, userNickname = ?, phoneNumber = ?, userMail = ?";

        try
        {
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, user.getUserName());
            pstmt.setString(2, user.getUserNickname());
            pstmt.setString(3, user.getPhoneNumber());
            pstmt.setString(4, user.getUserMail());

            return pstmt.executeUpdate();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally {
            try
            {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }
        }

        return -1;
    }

    public int delete(String id)
    {
        String query = "DELETE FROM USER WHERE userID = ?";

        try {
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, id);
            return pstmt.executeUpdate();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }
        }

        return -1;
    }
}
