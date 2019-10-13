package com.amazonaws.samples;

import java.util.List;
import java.io.File;
import com.amazonaws.services.s3.*;
import com.amazonaws.services.s3.model.Bucket;

public class UploadingImages {
	public static void main(String...str ) throws Exception{
		File file = new File("C:\\Users\\pulki\\Pictures\\Camera Roll\\img3.jpg");
		String key = "img_foo_bar_2.jpg";
		String bucketName = "nbc2";
		AmazonS3 client = AmazonS3ClientBuilder.defaultClient();
		try {
			List<Bucket> l = client.listBuckets();
			for(Bucket b:l) {
				System.out.println(b.getName());
			}
			client.putObject(bucketName, key, file);
		}catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}
}
