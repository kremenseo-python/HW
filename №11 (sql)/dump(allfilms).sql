--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

-- Started on 2019-12-14 15:02:58

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 16442)
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    gategory_id integer NOT NULL,
    name character varying(255),
    last_update integer
);


ALTER TABLE public.category OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16440)
-- Name: category_gategory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_gategory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_gategory_id_seq OWNER TO postgres;

--
-- TOC entry 2821 (class 0 OID 0)
-- Dependencies: 202
-- Name: category_gategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_gategory_id_seq OWNED BY public.category.gategory_id;


--
-- TOC entry 2687 (class 2604 OID 16445)
-- Name: category gategory_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN gategory_id SET DEFAULT nextval('public.category_gategory_id_seq'::regclass);


--
-- TOC entry 2815 (class 0 OID 16442)
-- Dependencies: 203
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (gategory_id, name, last_update) FROM stdin;
1	Hitman	2001
2	Titanic	1998
3	Prestige	2005
\.


--
-- TOC entry 2822 (class 0 OID 0)
-- Dependencies: 202
-- Name: category_gategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_gategory_id_seq', 3, true);


-- Completed on 2019-12-14 15:03:02

--
-- PostgreSQL database dump complete
--

