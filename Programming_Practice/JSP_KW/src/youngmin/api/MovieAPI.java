package youngmin.api;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Type;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

import com.google.gson.Gson;


public class MovieAPI {

    private static final String CLIENT_ID = "FhhvcGQ1FUHHAQtnt0O3";
    private static final String CLIENT_PW = "O0EkDob9SF";

    public String getJson(String searchStr)
    {
        BufferedReader br = null;
        HttpURLConnection urlConnection = null;
        try
        {
            String encSearchStr = URLEncoder.encode(searchStr, "UTF-8");
            int display = 20;
            String apiURL = "https://openapi.naver.com/v1/search/movie.json?query=" + encSearchStr;
            URL url = new URL(apiURL);
            urlConnection = (HttpURLConnection) url.openConnection();
            urlConnection.setRequestMethod("GET");
            urlConnection.setRequestProperty("X-Naver-Client-Id", CLIENT_ID);
            urlConnection.setRequestProperty("X-Naver-Client-Secret", CLIENT_PW);

            int responseCode = urlConnection.getResponseCode();
            if (responseCode == 200)
                br = new BufferedReader(new InputStreamReader(urlConnection.getInputStream(), StandardCharsets.UTF_8));
            else
                br = new BufferedReader(new InputStreamReader(urlConnection.getErrorStream(), StandardCharsets.UTF_8));
            StringBuilder result = new StringBuilder();
            String line = null;
            while ((line = br.readLine()) != null)
            {
                result.append(line);
            }
            return result.toString().trim();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                if (br != null) br.close();
                if (urlConnection != null) urlConnection.disconnect();
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }
        }

        return null;
    }

    public String getXML(String searchStr)
    {
        BufferedReader br = null;
        HttpURLConnection urlConnection = null;
        try
        {
            String encSearchStr = URLEncoder.encode(searchStr, "UTF-8");
            int display = 20;
            String apiURL = "https://openapi.naver.com/v1/search/movie.xml?query=" + encSearchStr;
            URL url = new URL(apiURL);
            urlConnection = (HttpURLConnection) url.openConnection();
            urlConnection.setRequestMethod("GET");
            urlConnection.setRequestProperty("X-Naver-Client-Id", CLIENT_ID);
            urlConnection.setRequestProperty("X-Naver-Client-Secret", CLIENT_PW);

            int responseCode = urlConnection.getResponseCode();
            if (responseCode == 200)
                br = new BufferedReader(new InputStreamReader(urlConnection.getInputStream(), StandardCharsets.UTF_8));
            else
                br = new BufferedReader(new InputStreamReader(urlConnection.getErrorStream(), StandardCharsets.UTF_8));
            StringBuilder result = new StringBuilder();
            String line = null;
            while ((line = br.readLine()) != null)
            {
                result.append(line).append(System.lineSeparator());
            }
            return result.toString();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                if (br != null) br.close();
                if (urlConnection != null) urlConnection.disconnect();
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }
        }

        return null;
    }

    public MovieInfoJO parseJsonToObject(String jsonData)
    {
//        Type joType = new TypeToken<Collection<MovieInfoJO>>(){}.getType();

        Gson gson = new Gson();

        return gson.fromJson(jsonData, MovieInfoJO.class);
    }
}
