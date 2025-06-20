-- Table: public.edwin_table

-- DROP TABLE IF EXISTS public.edwin_table;

CREATE TABLE IF NOT EXISTS public.edwin_table
(
    id character varying(64) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(64) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(64) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
                             data text COLLATE pg_catalog."default",
                             CONSTRAINT edwin_table_pkey PRIMARY KEY (id)
    )

    TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.edwin_table
    OWNER to testdb;
