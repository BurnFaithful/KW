package youngmin.bbs;

import java.sql.*;
import java.util.ArrayList;

public class ReviewbbsDAO {

    private Connection conn = null;
    private PreparedStatement pstmt = null;
    private ResultSet rs = null;

    public ReviewbbsDAO()
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

    public String getNowDate()
    {
        String query = "SELECT NOW()";

        try
        {
            pstmt = conn.prepareStatement(query);
            rs = pstmt.executeQuery();
            if (rs.next())
            {
                return rs.getString(1);
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

        return "";
    }

    public int getNextID()
    {
        String query = "SELECT reviewID FROM REVIEWBBS ORDER BY reviewID DESC";

        try
        {
            pstmt = conn.prepareStatement(query);
            rs = pstmt.executeQuery();

            if (rs.next())
            {
                return rs.getInt(1) + 1;
            }
            return 1;
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                if (rs != null)  rs.close();
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

    public ArrayList<ReviewbbsDTO> getBBSList()
    {
        String query = "SELECT * FROM REVIEWBBS ORDER BY reviewID DESC LIMIT 10";

        ArrayList<ReviewbbsDTO> bbsInfoList = new ArrayList<ReviewbbsDTO>();
        try
        {
            pstmt = conn.prepareStatement(query);
            rs = pstmt.executeQuery();

            while (rs.next())
            {
                ReviewbbsDTO bbsInfo = new ReviewbbsDTO();
                bbsInfo.setReviewID(rs.getInt(1));
                bbsInfo.setWriterID(rs.getString(2));
                bbsInfo.setWriterNickname(rs.getString(3));
                bbsInfo.setReviewTitle(rs.getString(4));
                bbsInfo.setReviewContent(rs.getString(5));
                bbsInfo.setReviewDate(rs.getString(6));
                bbsInfoList.add(bbsInfo);
            }
            return bbsInfoList;
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

        return bbsInfoList;
    }

    public ReviewbbsDTO getBBSInfo(int _reviewID)
    {
        String query = "SELECT writerID, writerNickname, reviewTitle, reviewContent, reviewDate FROM REVIEWBBS WHERE reviewID = ?";

        ReviewbbsDTO bbsInfo = new ReviewbbsDTO();
        try
        {
            pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, _reviewID);
            rs = pstmt.executeQuery();

            if (rs.next())
            {
                bbsInfo.setReviewID(_reviewID);
                bbsInfo.setWriterID(rs.getString(1));
                bbsInfo.setWriterNickname(rs.getString(2));
                bbsInfo.setReviewTitle(rs.getString(3));
                bbsInfo.setReviewContent(rs.getString(4));
                bbsInfo.setReviewDate(rs.getString(5));
                return bbsInfo;
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

        return bbsInfo;
    }

    public int write(String writerID, String writerNickname, String title, String content) {
        String query = "INSERT INTO REVIEWBBS VALUES(?, ?, ?, ?, ?, ?)";

        try
        {
            pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, new ReviewbbsDAO().getNextID());
            pstmt.setString(2, writerID);
            pstmt.setString(3, writerNickname);
            pstmt.setString(4, title);
            pstmt.setString(5, content);
            pstmt.setString(6, new ReviewbbsDAO().getNowDate());

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
        return -1; // DB 접속 오류
    }

    public int modify(int id, String title, String content)
    {
        String query = "UPDATE REVIEWBBS SET reviewTitle = ?, reviewContent = ? WHERE reviewID = ?";

        try
        {
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, title);
            pstmt.setString(2, content);
            pstmt.setInt(3, id);
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
        return -1; // DB Error
    }

    public int delete(int id)
    {
        String query = "DELETE FROM REVIEWBBS WHERE reviewID = ?";

        try
        {
            pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, id);
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
        return -1; // DB Error
    }
}
