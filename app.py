import streamlit as st
from PIL import Image

from ocr import extract_text
from budget import analyze_budget
from suggestions import generate_suggestions


st.set_page_config(
    page_title="SaveWise AI",
    page_icon="💰",
    layout="wide"
)

st.title("💰 SaveWise AI")
st.subheader("OCR-Based Intelligent Personal Budget & Savings Planner")

st.write(
    "Upload your monthly income and expense details as an image. "
    "SaveWise AI extracts the information and helps you plan your savings."
)

st.divider()

# Upload image
uploaded_file = st.file_uploader(
    "📸 Upload your monthly budget image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Budget",
        width=500
    )

    if st.button("🔍 Analyze My Budget"):

        with st.spinner("Reading your budget..."):

            extracted_text = extract_text(image)

        st.subheader("📝 Extracted Information")

        if extracted_text:

            st.text_area(
                "OCR Result",
                extracted_text,
                height=200
            )

            # Analyze budget
            result = analyze_budget(extracted_text)

            income = result["income"]
            expenses = result["expenses"]
            total_expense = result["total_expense"]
            balance = result["balance"]

            st.divider()

            st.subheader("📊 Budget Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Monthly Income",
                    f"₹{income:,.2f}"
                )

            with col2:
                st.metric(
                    "Total Expenses",
                    f"₹{total_expense:,.2f}"
                )

            with col3:
                st.metric(
                    "Available Balance",
                    f"₹{balance:,.2f}"
                )

            # Expense details
            if expenses:

                st.subheader("🧾 Expense Breakdown")

                for category, amount in expenses.items():

                    st.write(
                        f"**{category.title()}** : ₹{amount:,.2f}"
                    )

                # Chart
                st.subheader("📈 Expense Distribution")

                st.bar_chart(expenses)

            # Suggestions
            st.divider()

            st.subheader("💡 Smart Saving Suggestions")

            suggestions = generate_suggestions(
                income,
                expenses,
                total_expense,
                balance
            )

            for suggestion in suggestions:

                st.info(suggestion)

        else:

            st.warning(
                "No text could be detected. "
                "Please upload a clear budget image."
            )


# Goal planner
st.divider()

st.subheader("🎯 Savings Goal Planner")

col1, col2 = st.columns(2)

with col1:

    target_amount = st.number_input(
        "Target Savings Amount (₹)",
        min_value=0.0,
        step=1000.0
    )

with col2:

    target_months = st.number_input(
        "Target Duration (Months)",
        min_value=1,
        step=1
    )


if st.button("🎯 Calculate My Goal"):

    if target_amount > 0:

        required_monthly = target_amount / target_months

        st.success(
            f"You need to save approximately "
            f"**₹{required_monthly:,.2f} per month** "
            f"to reach your goal."
        )

    else:

        st.warning("Please enter a savings target.")
