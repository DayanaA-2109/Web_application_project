"""
DISPATCH//OS — Courier & Parcel Admin Monitoring Dashboard
Built with Streamlit (Python)

Run with:
    pip install streamlit pandas plotly
    streamlit run courier_admin_dashboard.py
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG + THEME COLORS
# ---------------------------------------------------------
st.set_page_config(
    page_title="DISPATCH//OS — Admin Console",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

BG = "#0B1220"
PANEL = "#121B2E"
LINE = "#1E2A42"
AMBER = "#F5A524"
CYAN = "#2DD4BF"
RED = "#F2545B"
VIOLET = "#8B7CF6"
TEXT = "#E7ECF5"
MUTED = "#8C9AB5"

# ---------------------------------------------------------
# GLOBAL CSS (dark "dispatch console" theme)
# ---------------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {BG};
        color: {TEXT};
        font-family: 'Inter', system-ui, sans-serif;
    }}
    section[data-testid="stSidebar"] {{
        background-color: {PANEL};
        border-right: 1px solid {LINE};
    }}
    div[data-testid="stMetric"] {{
        background-color: {PANEL};
        border: 1px solid {LINE};
        border-radius: 12px;
        padding: 14px 16px;
    }}
    div[data-testid="stMetricLabel"] {{
        color: {MUTED} !important;
    }}
    .block-container {{
        padding-top: 1.5rem;
    }}
    .status-pill {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 11px;
        font-family: monospace;
        letter-spacing: 0.4px;
        border-radius: 20px;
        padding: 3px 10px;
        text-transform: uppercase;
    }}
    .dot {{
        width: 6px; height: 6px; border-radius: 50%; display: inline-block;
    }}
    thead tr th {{
        color: {MUTED} !important;
        font-family: monospace;
        font-size: 11px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# MOCK DATA
# ---------------------------------------------------------
traffic_df = pd.DataFrame({
    "time": ["00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00"],
    "parcels": [12, 8, 24, 61, 78, 92, 70, 41],
})

status_split = pd.DataFrame({
    "status": ["Delivered", "In Transit", "Delayed", "Cancelled"],
    "value": [612, 248, 37, 14],
})
status_colors = {"Delivered": CYAN, "In Transit": AMBER, "Delayed": RED, "Cancelled": VIOLET}

zone_load = pd.DataFrame({
    "zone": ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"],
    "load": [82, 64, 95, 45, 70],
})

users_df = pd.DataFrame([
    {"ID": "U-1042", "Name": "Asha Verma", "Email": "asha.verma@mail.com", "Orders": 23, "Joined": "2024-02-11", "Status": "active"},
    {"ID": "U-1043", "Name": "Rohit Malhotra", "Email": "rohit.m@mail.com", "Orders": 7, "Joined": "2024-06-03", "Status": "active"},
    {"ID": "U-1044", "Name": "Priya Nair", "Email": "priya.nair@mail.com", "Orders": 41, "Joined": "2023-11-22", "Status": "suspended"},
    {"ID": "U-1045", "Name": "Imran Sheikh", "Email": "imran.s@mail.com", "Orders": 2, "Joined": "2025-01-09", "Status": "active"},
    {"ID": "U-1046", "Name": "Kavya Reddy", "Email": "kavya.r@mail.com", "Orders": 15, "Joined": "2024-09-18", "Status": "inactive"},
])

admins_df = pd.DataFrame([
    {"ID": "A-01", "Name": "Sandeep Kulkarni", "Role": "Super Admin", "Access": "Full", "Last seen": "2 min ago", "Status": "active"},
    {"ID": "A-02", "Name": "Meera Joshi", "Role": "Ops Manager", "Access": "Logistics, Users", "Last seen": "14 min ago", "Status": "active"},
    {"ID": "A-03", "Name": "Farhan Ali", "Role": "Support Lead", "Access": "Tickets, Users", "Last seen": "3 hrs ago", "Status": "idle"},
    {"ID": "A-04", "Name": "Divya Pillai", "Role": "Finance Admin", "Access": "Payments, Reports", "Last seen": "1 day ago", "Status": "offline"},
])

orders_df = pd.DataFrame([
    {"Order": "ORD-8841", "Customer": "Asha Verma", "Merchant": "Urban Threads", "Value": "₹2,340", "Status": "delivered"},
    {"Order": "ORD-8842", "Customer": "Rohit Malhotra", "Merchant": "GreenLeaf Mart", "Value": "₹890", "Status": "in-transit"},
    {"Order": "ORD-8843", "Customer": "Priya Nair", "Merchant": "TechNest", "Value": "₹14,200", "Status": "delayed"},
    {"Order": "ORD-8844", "Customer": "Imran Sheikh", "Merchant": "Spice Route", "Value": "₹560", "Status": "delivered"},
    {"Order": "ORD-8845", "Customer": "Kavya Reddy", "Merchant": "Urban Threads", "Value": "₹1,120", "Status": "cancelled"},
])

agents_df = pd.DataFrame([
    {"ID": "DA-201", "Name": "Vikram Singh", "Zone": "Zone A", "Active": True, "Parcels": 14, "Rating": 4.8, "ETA": "On time"},
    {"ID": "DA-202", "Name": "Sunita Devi", "Zone": "Zone C", "Active": True, "Parcels": 21, "Rating": 4.6, "ETA": "Delayed 12m"},
    {"ID": "DA-203", "Name": "Manoj Kumar", "Zone": "Zone B", "Active": False, "Parcels": 0, "Rating": 4.9, "ETA": "Off duty"},
    {"ID": "DA-204", "Name": "Ritika Bose", "Zone": "Zone E", "Active": True, "Parcels": 9, "Rating": 4.7, "ETA": "On time"},
])

STATUS_COLORS = {
    "active": CYAN, "delivered": CYAN,
    "in-transit": AMBER, "idle": AMBER,
    "delayed": RED, "suspended": RED,
    "cancelled": VIOLET,
    "inactive": MUTED, "offline": MUTED,
}


def status_pill(status: str) -> str:
    color = STATUS_COLORS.get(status, MUTED)
    return (
        f'<span class="status-pill" style="color:{color};'
        f'border:1px solid {color}55;background:{color}14;">'
        f'<span class="dot" style="background:{color};"></span>{status}</span>'
    )


def render_table_with_status(df: pd.DataFrame, status_col: str = "Status"):
    """Render a dataframe as HTML with colored status pills."""
    display_df = df.copy()
    display_df[status_col] = display_df[status_col].apply(status_pill)
    st.markdown(
        display_df.to_html(escape=False, index=False),
        unsafe_allow_html=True,
    )


def plotly_dark_layout(fig):
    fig.update_layout(
        plot_bgcolor=PANEL,
        paper_bgcolor=PANEL,
        font_color=TEXT,
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(font=dict(color=MUTED)),
    )
    fig.update_xaxes(gridcolor=LINE, color=MUTED)
    fig.update_yaxes(gridcolor=LINE, color=MUTED)
    return fig


# ---------------------------------------------------------
# SIDEBAR NAV
# ---------------------------------------------------------
st.sidebar.markdown(
    f"""
    <div style="display:flex;align-items:center;gap:10px;padding:0 4px 16px;">
        <div style="width:32px;height:32px;border-radius:8px;background:{AMBER}22;
            display:flex;align-items:center;justify-content:center;font-size:16px;">📦</div>
        <div>
            <div style="font-weight:700;font-size:14px;color:{TEXT};">DISPATCH//OS</div>
            <div style="font-size:10px;color:{MUTED};font-family:monospace;">admin console</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "Navigate",
    ["Overview", "Users", "Admins", "E-commerce", "Delivery Agents"],
    label_visibility="collapsed",
)

st.sidebar.markdown(
    f"""
    <div style="margin-top:24px;padding-top:12px;border-top:1px solid {LINE};
        font-size:10px;color:{MUTED};font-family:monospace;">
        SYSTEM STATUS<br><span style="color:{CYAN};">● </span>All services nominal
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# TOP SEARCH BAR (shared across tabs that have tables)
# ---------------------------------------------------------
search_placeholders = {
    "Users": "Search users by name, email or ID…",
    "Admins": "Search admins by name or role…",
    "E-commerce": "Search orders by ID, customer, merchant…",
    "Delivery Agents": "Search agents by name, zone or ID…",
}

top_col1, top_col2 = st.columns([3, 1])
with top_col1:
    st.markdown(f"## {page}")
query = ""
if page in search_placeholders:
    query = st.text_input(
        "Search", placeholder=search_placeholders[page], label_visibility="collapsed"
    )

# ---------------------------------------------------------
# PAGE: OVERVIEW
# ---------------------------------------------------------
if page == "Overview":
    st.caption("Real-time pulse of orders, dispatch and field operations.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Registered Users", "8,214", "+4.2%")
    c2.metric("Orders Today", "911", "+11.8%")
    c3.metric("Active Agents", "142", "-2.1%")
    c4.metric("Open Escalations", "9", "+3")

    col_a, col_b = st.columns([2, 1])

    with col_a:
        st.markdown("**Dispatch Volume** — parcels per 3-hour window, today")
        fig = px.area(traffic_df, x="time", y="parcels", color_discrete_sequence=[AMBER])
        fig.update_traces(line=dict(width=2), fillcolor=f"{AMBER}40")
        st.plotly_chart(plotly_dark_layout(fig), use_container_width=True)

    with col_b:
        st.markdown("**Status Split** — live order status mix")
        fig = px.pie(
            status_split, names="status", values="value", hole=0.55,
            color="status", color_discrete_map=status_colors,
        )
        fig.update_traces(textfont_color=TEXT)
        st.plotly_chart(plotly_dark_layout(fig), use_container_width=True)

    st.markdown("**Zone Load** — parcel load currently assigned, by delivery zone")
    bar_colors = [RED if v > 85 else AMBER if v > 65 else CYAN for v in zone_load["load"]]
    fig = go.Figure(go.Bar(x=zone_load["zone"], y=zone_load["load"], marker_color=bar_colors))
    st.plotly_chart(plotly_dark_layout(fig), use_container_width=True)

# ---------------------------------------------------------
# PAGE: USERS
# ---------------------------------------------------------
elif page == "Users":
    st.caption("Manage customer accounts placing parcel and courier orders.")
    filtered = users_df[
        users_df.apply(lambda r: query.lower() in " ".join(map(str, r)).lower(), axis=1)
    ] if query else users_df
    st.markdown(f"*{len(filtered)} of {len(users_df)} accounts shown*")
    render_table_with_status(filtered)

# ---------------------------------------------------------
# PAGE: ADMINS
# ---------------------------------------------------------
elif page == "Admins":
    st.caption("Manage staff seats and their access scope across the console.")
    filtered = admins_df[
        admins_df.apply(lambda r: query.lower() in " ".join(map(str, r)).lower(), axis=1)
    ] if query else admins_df
    st.markdown(f"*{len(filtered)} of {len(admins_df)} admin seats*")
    render_table_with_status(filtered)

# ---------------------------------------------------------
# PAGE: E-COMMERCE
# ---------------------------------------------------------
elif page == "E-commerce":
    st.caption("Track marketplace orders feeding into the courier pipeline.")
    filtered = orders_df[
        orders_df.apply(lambda r: query.lower() in " ".join(map(str, r)).lower(), axis=1)
    ] if query else orders_df
    st.markdown(f"*{len(filtered)} of {len(orders_df)} orders shown*")
    render_table_with_status(filtered)

# ---------------------------------------------------------
# PAGE: DELIVERY AGENTS
# ---------------------------------------------------------
elif page == "Delivery Agents":
    st.caption("Monitor delivery agents currently assigned to live parcels.")
    filtered = agents_df[
        agents_df.apply(lambda r: query.lower() in " ".join(map(str, r)).lower(), axis=1)
    ] if query else agents_df

    cols = st.columns(len(filtered)) if len(filtered) > 0 else [st]
    for col, (_, a) in zip(cols, filtered.iterrows()):
        with col:
            dot_color = CYAN if a["Active"] else MUTED
            eta_color = CYAN if a["ETA"] == "On time" else (MUTED if a["ETA"] == "Off duty" else RED)
            st.markdown(
                f"""
                <div style="background:{PANEL};border:1px solid {LINE};border-radius:14px;padding:16px;">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <div>
                            <div style="font-weight:600;font-size:13px;color:{TEXT};">🚚 {a['Name']}</div>
                            <div style="font-size:11px;color:{MUTED};font-family:monospace;">{a['ID']} · {a['Zone']}</div>
                        </div>
                        <span style="width:8px;height:8px;border-radius:50%;background:{dot_color};display:inline-block;"></span>
                    </div>
                    <div style="display:flex;justify-content:space-between;margin-top:14px;font-size:12px;">
                        <div><div style="color:{MUTED};">Parcels</div>
                            <div style="font-family:monospace;font-weight:600;color:{TEXT};">{a['Parcels']}</div></div>
                        <div><div style="color:{MUTED};">Rating</div>
                            <div style="font-family:monospace;font-weight:600;color:{TEXT};">{a['Rating']}★</div></div>
                        <div style="text-align:right;"><div style="color:{MUTED};">ETA</div>
                            <div style="font-family:monospace;font-weight:600;color:{eta_color};">{a['ETA']}</div></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            