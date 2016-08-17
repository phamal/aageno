package org.yaad.rest;


import com.google.gson.Gson;
import org.yaad.dtos.HashTag;

import javax.ws.rs.GET;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.Path;
import javax.ws.rs.core.Response;

@Path("/api")
public class YaadResource {

	@GET
	@Path("/name")
	public Response getMsg(@PathParam("name") String name) {

		String output = "Name is : " + name;

		return Response.status(200).entity(output).build();

	}

	@GET
	@Path("/hashtags")
	public Response getHashTags() {

		HashTag hashTag = new HashTag();
		hashTag.setHashtag("account");
		Gson gson = new Gson();

		return Response.status(200).entity(gson.toJson(hashTag)).build();

	}

}