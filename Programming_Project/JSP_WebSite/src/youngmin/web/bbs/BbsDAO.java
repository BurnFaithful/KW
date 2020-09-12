package youngmin.web.bbs;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

public class BbsDAO {

    private Connection conn = null;
    private ResultSet rs = null;

    public BbsDAO()
    {
        try
        {
            Class.forName("com.mysql.cj.jdbc.Driver");

            String dbUrl = "jdbc:mysql://localhost:3306/youngmin?serverTimezone=Asia/Seoul";
            String id = "root";
            String pw = "cout49!";
            conn = DriverManager.getConnection(dbUrl, id, pw);

        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }

    public String getDate()
    {
        String query = "SELECT NOW()";
        try
        {
            PreparedStatement pstmt = conn.prepareStatement(query);
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
        return ""; // DB Error
    }

    public int getNext()
    {
        String query = "SELECT bbsID FROM BBS ORDER BY bbsID DESC";
        try
        {
            PreparedStatement pstmt = conn.prepareStatement(query);
            rs = pstmt.executeQuery();
            if (rs.next())
            {
                return rs.getInt(1) + 1;
            }
            return 1; // 첫 게시물인 경우
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return -1; // DB Error
    }

    public int write(String bbsTitle, String userId, String bbsContent)
    {
        String query = "INSERT into BBS VALUES (?, ?, ?, ?, ?, ?)";
        try
        {
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, getNext());
            pstmt.setString(2, bbsTitle);
            pstmt.setString(3, userId);
            pstmt.setString(4, getDate());
            pstmt.setString(5, bbsContent);
            pstmt.setInt(6, 1);
            return pstmt.executeUpdate();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return -1; // DB Error
    }

    public ArrayList<Bbs> getList(int pageNum)
    {
        String query = "SELECT * FROM BBS WHERE bbsID < ? AND bbsAvailable = 1 ORDER BY bbsID DESC LIMIT 10";
        ArrayList<Bbs> list = new ArrayList<Bbs>();
        try
        {
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, getNext() - (pageNum - 1) * 10);
            rs = pstmt.executeQuery();
            while (rs.next())
            {
                Bbs bbs = new Bbs();
                bbs.setBbsID(rs.getInt(1));
                bbs.setBbsTitle(rs.getString(2));
                bbs.setUserID(rs.getString(3));
                bbs.setBbsDate(rs.getString(4));
                bbs.setBbsContent(rs.getString(5));
                bbs.setBbsAvailable(rs.getInt(6));
                list.add(bbs);
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return list;
    }

    public boolean nextPage(int pageNum)
    {
        String query = "SELECT * FROM BBS WHERE bbsID < ? AND bbsAvailable = 1";
        ArrayList<Bbs> list = new ArrayList<Bbs>();
        try
        {
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, getNext() - (pageNum - 1) * 10);
            rs = pstmt.executeQuery();
            if (rs.next())
                return true;
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return false;
    }

    public Bbs getBbs(int bbsID)
    {
        String query = "SELECT * FROM BBS WHERE bbsID = ?";
        try
        {
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, bbsID);
            rs = pstmt.executeQuery();
            if (rs.next())
            {
                Bbs bbs = new Bbs();
                bbs.setBbsID(rs.getInt(1));
                bbs.setBbsTitle(rs.getString(2));
                bbs.setUserID(rs.getString(3));
                bbs.setBbsDate(rs.getString(4));
                bbs.setBbsContent(rs.getString(5));
                bbs.setBbsAvailable(rs.getInt(6));
                return bbs;
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return null;
    }

    public int update(int bbsId, String updateTitle, String updateContent)
    {
        String query = "UPDATE BBS SET bbsTitle = ?, bbsContent = ? WHERE bbsID = ?";
        try
        {
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setString(1, updateTitle);
            pstmt.setString(2, updateContent);
            pstmt.setInt(3, bbsId);
            return pstmt.executeUpdate();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return -1; // DB Error
    }

    public int delete(int bbsID)
    {
        String query = "UPDATE BBS SET bbsAvailable = 0 WHERE bbsID = ?";
        try
        {
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, bbsID);
            return pstmt.executeUpdate();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return -1; // DB Error
    }
}
