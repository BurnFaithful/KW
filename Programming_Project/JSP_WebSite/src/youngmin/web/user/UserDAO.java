package youngmin.web.user;

import java.sql.*;
import java.util.ArrayList;

public class UserDAO {

	private Connection conn = null;
	private PreparedStatement pstmt = null;
	private ResultSet rs = null;
	
	public UserDAO()
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

	public ArrayList<User> getUserList()
	{
		String query = "SELECT * FROM USER WHERE id != ? ORDER BY id DESC";
		ArrayList<User> userList = new ArrayList<User>();
		try
		{
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, "admin");
			rs = pstmt.executeQuery();

			while (rs.next())
			{
				User tempUser = new User();
				tempUser.setId(rs.getString(1));
				tempUser.setPassword(rs.getString(2));
				tempUser.setName(rs.getString(3));
				tempUser.setAge(rs.getInt(4));
				tempUser.setEmail(rs.getString(5));
				tempUser.setPhoneNumber(rs.getString(6));
				userList.add(tempUser);
			}
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}

		return userList;
	}
	
	public int login(String inputId, String inputPw)
	{
		String query = "SELECT password FROM USER WHERE id = ?";
		try
		{
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, inputId);
			rs = pstmt.executeQuery();
			
			if (rs.next())
			{
				if (rs.getString(1).equals(inputPw))
					return 1;
				else
					return 0;
			}
			return -1;
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}

		return -2;
	}
	
	public int join(User user)
	{
		String query = "INSERT into USER VALUES (?, ?, ?, ?, ?, ?, DEFAULT)";
		try
		{
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, user.getId());
			pstmt.setString(2, user.getPassword());
			pstmt.setString(3, user.getName());
			pstmt.setInt(4, user.getAge());
			pstmt.setString(5, user.getEmail());
			pstmt.setString(6, user.getPhoneNumber());
			return pstmt.executeUpdate();
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
		
		return -1; // Exist ID
	}

	public int deleteUser(String userId)
	{
		String query = "DELETE FROM USER WHERE id = ?";

		try
		{
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, userId);
			return pstmt.executeUpdate();
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}

		return -1;
	}
}
