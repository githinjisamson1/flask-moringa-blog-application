import React from "react";
import "./signup.css";
import { useFormik } from "formik";
import * as yup from "yup";
import moringaLogo from "../../assets/moringaLogo.png";
import { useNavigate } from "react-router-dom";

// signup
const Signup = () => {
  const navigate = useNavigate();

  // 3 args => initialValues, validationSchema, onSubmit
  const formik = useFormik({
    initialValues: {
      username: "",
      full_name: "",
      email: "",
      password: "",
      confirm_password: "",
    },

    validationSchema: yup.object().shape({
      username: yup.string().required("Username required"),
      full_name: yup.string().required("Full Name required"),
      email: yup
        .string()
        .email("Invalid email address")
        .required("Email required"),
      password: yup
        .string()
        .min(8, "Password must be atleast 8 characters")
        .required("Password required"),
      confirm_password: yup
        .string()
        .oneOf([yup.ref("password"), null], "Passwords must match")
        .required("Please confirm password"),
    }),

    onSubmit: (values, { resetForm }) => {
      console.log(values);

      // proxy: http://127.0.0.1:5555
      // fetch API => /users : register user
      fetch("/users", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify(values),
      })
        .then((response) => {
          if (response.ok) {
            alert("Account created successfully");
            navigate("/signin");

            // clear form values
            resetForm();
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
    <div className="container">
      <div className="sign-up-form-container">
        {/* left side */}
        <div className="left">
          <img src={moringaLogo} alt="" />
        </div>

        {/* right side */}
        <form className="signup-form" onSubmit={formik.handleSubmit}>
          <h2 className="primary-title">Register</h2>
          <p className="secondary-title">It's completely free</p>

          <div className="form-control">
            <label htmlFor="username">Username</label>
            <br />
            <input
              type="text"
              id="username"
              name="username"
              value={formik.values.username}
              onChange={formik.handleChange}
              placeholder="e.g., johndoe1"
            />
            {formik.touched.username && formik.errors.username ? (
              <div className="error">{formik.errors.username}</div>
            ) : null}
          </div>

          <div className="form-control">
            <label htmlFor="full_name">Full Name</label>
            <br />
            <input
              type="text"
              id="full_name"
              name="full_name"
              value={formik.values.full_name}
              onChange={formik.handleChange}
              placeholder="e.g., John Doe"
            />
            {formik.touched.full_name && formik.errors.full_name ? (
              <div className="error">{formik.errors.full_name}</div>
            ) : null}
          </div>

          <div className="form-control">
            <label htmlFor="email">Email</label>
            <br />
            <input
              type="email"
              id="email"
              name="email"
              value={formik.values.email}
              onChange={formik.handleChange}
              placeholder="e.g., john.doe@student.moringaschool.com"
            />
            {formik.touched.email && formik.errors.email ? (
              <div className="error">{formik.errors.email}</div>
            ) : null}
          </div>

          <div className="form-control">
            <label htmlFor="password">Password</label>
            <br />
            <input
              type="password"
              id="password"
              name="password"
              value={formik.values.password}
              onChange={formik.handleChange}
              placeholder="Enter password"
            />
            {formik.touched.password && formik.errors.password ? (
              <div className="error">{formik.errors.password}</div>
            ) : null}
          </div>

          <div className="form-control">
            <label htmlFor="confirm_password">Confirm Password</label>
            <br />
            <input
              type="password"
              id="confirm_password"
              name="confirm_password"
              value={formik.values.confirm_password}
              onChange={formik.handleChange}
              placeholder="Confirm password"
            />
            {formik.touched.confirm_password &&
            formik.errors.confirm_password ? (
              <div className="error">{formik.errors.confirm_password}</div>
            ) : null}
          </div>

          <div className="terms-and-conditions">
            <input type="checkbox" /> I have read and agreed to be bound by the
            terms and conditions of using this application.
          </div>

          <div className="create-account-container">
            <button className="create-account-btn" type="submit">
              Create Account
            </button>
          </div>

          <p className="already-have-account">
            Already have an account?
            <span
              onClick={() => {
                navigate("/signin");
              }}
            >
              {" "}
              Sign in.
            </span>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Signup;
