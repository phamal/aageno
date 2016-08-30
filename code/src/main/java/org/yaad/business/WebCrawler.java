package org.yaad.business;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by phamal on 8/17/16.
 */
public class WebCrawler
{
	public String crawlSite(String siteUrl){
		String summary = "";
		URL url;
		InputStream is = null;
		DataInputStream dis;
		String line;

		try {
			url = new URL(siteUrl);
			is = url.openStream();  // throws an IOException
			dis = new DataInputStream(new BufferedInputStream(is));

			while ( (line = dis.readLine()) != null) {
				System.out.println(line);
				summary += "line";
			}
		} catch (MalformedURLException mue) {
			mue.printStackTrace();
		} catch (IOException ioe) {
			ioe.printStackTrace();
		} finally {
			try {
				is.close();
			} catch (IOException ioe) {
				// nothing to see here
			}
		}

		return summary;
	}
}
