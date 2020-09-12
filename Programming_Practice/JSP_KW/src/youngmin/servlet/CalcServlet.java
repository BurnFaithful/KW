package youngmin.servlet;

import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;


@WebServlet(description = "Calc1", urlPatterns = { "/CalcServlet" })
public class CalcServlet extends HttpServlet {

	private static final long serialVersionUID = 1L;

	public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		doPost(request, response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	
		int num1, num2;
		int result;
		String op;

		response.setContentType("text/html; charset=UTF-8");

		PrintWriter out = response.getWriter();

		num1 = Integer.parseInt(request.getParameter("num1"));
		num2 = Integer.parseInt(request.getParameter("num2"));
		op = request.getParameter("operator");
		
		result = calc(num1, num2, op);

		out.println("<html>");
		out.println("<head><title>계산기</title></head>");
		out.println("<body><center>");
		out.println("<h2>계산 결과</h2>");
		out.println("<hr>");
		out.println(num1 + " " + op + " " + num2 + " = " + result);
		out.println("</body></html>");
	}


	public int calc(int num1, int num2, String op)
	{
		int result = 0;

		if(op.equals("+"))
			result = num1 + num2;
		else if(op.equals("-"))
			result = num1 - num2;
		else if(op.equals("*"))
			result = num1 * num2;
		else if(op.equals("/"))
			result = num1 / num2;

		return result;
	}
}