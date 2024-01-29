import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import "./createPostForm.css";
import { useGlobalUserContext } from "../../context/authContext";
import { useNavigate } from "react-router-dom";

const CreatePostForm = () => {
  const { currentUser } = useGlobalUserContext();

  const navigate=useNavigate()

  const formik = useFormik({
    initialValues: {
      phase: "",
      title: "",
      content: "",
      resources: "",
    },
    validationSchema: Yup.object({
      phase: Yup.number().required("Phase required"),
      title: Yup.string().required("Title required"),
      content: Yup.string().required("Content required"),
      resources: Yup.string().url("Invalid URL"),
    }),

    onSubmit: (values, {resetForm}) => {
      console.log(values);

      // fetch API
      fetch("/posts", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          Authorization: `Bearer ${localStorage.getItem("auth_token")}`,
        },
        body: JSON.stringify(values),
      })
        .then((response) => {
          if (response.ok) {
            resetForm()
            navigate("/dashboard")
            return response.json();
          }
        })
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  });
  return (
    <div className="create-post-form-container">
      <form
        action=""
        className="create-post-form"
        onSubmit={formik.handleSubmit}
      >
        <h2 className="create-post-title">Create New Post</h2>

        <div className="form-control">
          <label htmlFor="">Phase</label>
          <input
            type="number"
            placeholder="e.g.,0, 1, 2, 3, 4, 5"
            name="phase"
            id="phase"
            value={formik.values.phase}
            onChange={formik.handleChange}
          />
          {formik.touched && formik.errors.phase ? (
            <div className="error">*{formik.errors.phase}</div>
          ) : null}
        </div>

        <div className="form-control">
          <label htmlFor="">Title</label>
          <input
            type="text"
            placeholder="Enter post title"
            name="title"
            id="title"
            value={formik.values.title}
            onChange={formik.handleChange}
          />
          {formik.touched && formik.errors.title ? (
            <div className="error">*{formik.errors.title}</div>
          ) : null}
        </div>

        <div className="form-control">
          <label htmlFor="">Content</label>
          <textarea
            cols="30"
            rows="10"
            name="content"
            id="content"
            value={formik.values.content}
            onChange={formik.handleChange}
          ></textarea>
          {formik.touched && formik.errors.content ? (
            <div className="error">*{formik.errors.content}</div>
          ) : null}
        </div>

        <div className="form-control">
          <label htmlFor="">Resources</label>
          <input
            type="url"
            placeholder="Enter link to resource"
            name="resources"
            id="resources"
            value={formik.values.resources}
            onChange={formik.handleChange}
          />
          {formik.touched && formik.errors.resources ? (
            <div className="error">*{formik.errors.resources}</div>
          ) : null}
        </div>

        <button type="submit" className="create-post-form-btn">
          Create New Post
        </button>
      </form>
    </div>
  );
};

export default CreatePostForm;
