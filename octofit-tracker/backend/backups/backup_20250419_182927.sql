DROP TABLE IF EXISTS "django_migrations" CASCADE;
DROP TABLE IF EXISTS "django_content_type" CASCADE;
DROP TABLE IF EXISTS "auth_permission" CASCADE;
DROP TABLE IF EXISTS "auth_group" CASCADE;
DROP TABLE IF EXISTS "auth_group_permissions" CASCADE;
DROP TABLE IF EXISTS "auth_user" CASCADE;
DROP TABLE IF EXISTS "auth_user_groups" CASCADE;
DROP TABLE IF EXISTS "auth_user_user_permissions" CASCADE;
DROP TABLE IF EXISTS "django_admin_log" CASCADE;
DROP TABLE IF EXISTS "octofit_tracker_activity" CASCADE;
DROP TABLE IF EXISTS "octofit_tracker_leaderboard" CASCADE;
DROP TABLE IF EXISTS "octofit_tracker_team" CASCADE;
DROP TABLE IF EXISTS "octofit_tracker_user" CASCADE;
DROP TABLE IF EXISTS "octofit_tracker_workout" CASCADE;
DROP TABLE IF EXISTS "django_session" CASCADE;

CREATE TABLE "django_migrations" (
    "id" bigint NOT NULL,
    "app" character varying(255) NOT NULL,
    "name" character varying(255) NOT NULL,
    "applied" timestamp with time zone NOT NULL
);
ALTER TABLE "django_migrations" ADD PRIMARY KEY ("id");
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('1', 'contenttypes', '0001_initial', '2025-04-19 18:04:35.169768+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('2', 'auth', '0001_initial', '2025-04-19 18:04:35.237062+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('3', 'admin', '0001_initial', '2025-04-19 18:04:35.255610+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2025-04-19 18:04:35.261535+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2025-04-19 18:04:35.267737+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2025-04-19 18:04:35.280589+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2025-04-19 18:04:35.287088+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2025-04-19 18:04:35.293211+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('9', 'auth', '0004_alter_user_username_opts', '2025-04-19 18:04:35.299162+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2025-04-19 18:04:35.306124+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2025-04-19 18:04:35.308173+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2025-04-19 18:04:35.313997+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2025-04-19 18:04:35.323323+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2025-04-19 18:04:35.329981+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('15', 'auth', '0010_alter_group_name_max_length', '2025-04-19 18:04:35.338106+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('16', 'auth', '0011_update_proxy_permissions', '2025-04-19 18:04:35.344294+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('17', 'auth', '0012_alter_user_first_name_max_length', '2025-04-19 18:04:35.350210+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('18', 'octofit_tracker', '0001_initial', '2025-04-19 18:04:35.382651+00:00');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES ('19', 'sessions', '0001_initial', '2025-04-19 18:04:35.395014+00:00');

CREATE TABLE "django_content_type" (
    "id" integer NOT NULL,
    "app_label" character varying(100) NOT NULL,
    "model" character varying(100) NOT NULL
);
ALTER TABLE "django_content_type" ADD PRIMARY KEY ("id");
ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label");
ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label");
ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("model");
ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("model");
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('1', 'admin', 'logentry');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('2', 'auth', 'permission');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('3', 'auth', 'group');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('4', 'auth', 'user');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('6', 'sessions', 'session');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('7', 'octofit_tracker', 'activity');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('8', 'octofit_tracker', 'leaderboard');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('9', 'octofit_tracker', 'team');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('10', 'octofit_tracker', 'user');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES ('11', 'octofit_tracker', 'workout');

CREATE TABLE "auth_permission" (
    "id" integer NOT NULL,
    "name" character varying(255) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" character varying(100) NOT NULL
);
ALTER TABLE "auth_permission" ADD PRIMARY KEY ("id");
ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id");
ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id");
ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("codename");
ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("codename");
ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id");
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('25', 'Can add activity', '7', 'add_activity');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('26', 'Can change activity', '7', 'change_activity');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('27', 'Can delete activity', '7', 'delete_activity');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('28', 'Can view activity', '7', 'view_activity');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('29', 'Can add leaderboard', '8', 'add_leaderboard');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('30', 'Can change leaderboard', '8', 'change_leaderboard');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('31', 'Can delete leaderboard', '8', 'delete_leaderboard');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('32', 'Can view leaderboard', '8', 'view_leaderboard');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('33', 'Can add team', '9', 'add_team');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('34', 'Can change team', '9', 'change_team');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('35', 'Can delete team', '9', 'delete_team');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('36', 'Can view team', '9', 'view_team');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('37', 'Can add user', '10', 'add_user');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('38', 'Can change user', '10', 'change_user');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('39', 'Can delete user', '10', 'delete_user');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('40', 'Can view user', '10', 'view_user');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('41', 'Can add workout', '11', 'add_workout');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('42', 'Can change workout', '11', 'change_workout');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('43', 'Can delete workout', '11', 'delete_workout');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES ('44', 'Can view workout', '11', 'view_workout');

CREATE TABLE "auth_group" (
    "id" integer NOT NULL,
    "name" character varying(150) NOT NULL
);
ALTER TABLE "auth_group" ADD PRIMARY KEY ("id");
ALTER TABLE "auth_group" ADD CONSTRAINT "auth_group_name_key" UNIQUE ("name");

CREATE TABLE "auth_group_permissions" (
    "id" bigint NOT NULL,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL
);
ALTER TABLE "auth_group_permissions" ADD PRIMARY KEY ("id");
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id");
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id");
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("permission_id");
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("permission_id");
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id");
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id");

CREATE TABLE "auth_user" (
    "id" integer NOT NULL,
    "password" character varying(128) NOT NULL,
    "last_login" timestamp with time zone,
    "is_superuser" boolean NOT NULL,
    "username" character varying(150) NOT NULL,
    "first_name" character varying(150) NOT NULL,
    "last_name" character varying(150) NOT NULL,
    "email" character varying(254) NOT NULL,
    "is_staff" boolean NOT NULL,
    "is_active" boolean NOT NULL,
    "date_joined" timestamp with time zone NOT NULL
);
ALTER TABLE "auth_user" ADD PRIMARY KEY ("id");
ALTER TABLE "auth_user" ADD CONSTRAINT "auth_user_username_key" UNIQUE ("username");
INSERT INTO "auth_user" ("id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") VALUES ('1', 'pbkdf2_sha256$390000$NKDogu9pyTsG6XWbZzZNXe$hE4tvTlNi50dbUAjJGXMYgnqTfGo6C8Kc35vCLALBHA=', '2025-04-19 18:10:14.957758+00:00', 'True', 'admin', '', '', 'admin@hr.com', 'True', 'True', '2025-04-19 18:09:49.437659+00:00');
INSERT INTO "auth_user" ("id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") VALUES ('2', 'pbkdf2_sha256$390000$rlDBffBhCrnxjShrDYZQ0t$YslyR2DxFe1q6xRKdtwGhDYhed1yqRATIo0gIt5GQ1I=', NULL, 'True', 'admin2', '', '', 'admin2@example.com', 'True', 'True', '2025-04-19 18:17:48.595037+00:00');

CREATE TABLE "auth_user_groups" (
    "id" bigint NOT NULL,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL
);
ALTER TABLE "auth_user_groups" ADD PRIMARY KEY ("id");
ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id");
ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id");
ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("group_id");
ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("group_id");
ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id");
ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id");

CREATE TABLE "auth_user_user_permissions" (
    "id" bigint NOT NULL,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL
);
ALTER TABLE "auth_user_user_permissions" ADD PRIMARY KEY ("id");
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id");
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id");
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("permission_id");
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("permission_id");
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id");
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id");

CREATE TABLE "django_admin_log" (
    "id" integer NOT NULL,
    "action_time" timestamp with time zone NOT NULL,
    "object_id" text,
    "object_repr" character varying(200) NOT NULL,
    "action_flag" smallint NOT NULL,
    "change_message" text NOT NULL,
    "content_type_id" integer,
    "user_id" integer NOT NULL
);
ALTER TABLE "django_admin_log" ADD PRIMARY KEY ("id");
ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id");
ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id");

CREATE TABLE "octofit_tracker_activity" (
    "id" bigint NOT NULL,
    "user" character varying(254) NOT NULL,
    "type" character varying(100) NOT NULL,
    "duration" integer NOT NULL,
    "date" date NOT NULL
);
ALTER TABLE "octofit_tracker_activity" ADD PRIMARY KEY ("id");

CREATE TABLE "octofit_tracker_leaderboard" (
    "id" bigint NOT NULL,
    "user" character varying(254) NOT NULL,
    "points" integer NOT NULL
);
ALTER TABLE "octofit_tracker_leaderboard" ADD PRIMARY KEY ("id");
ALTER TABLE "octofit_tracker_leaderboard" ADD CONSTRAINT "octofit_tracker_leaderboard_user_key" UNIQUE ("user");

CREATE TABLE "octofit_tracker_team" (
    "id" bigint NOT NULL,
    "name" character varying(100) NOT NULL,
    "members" jsonb NOT NULL
);
ALTER TABLE "octofit_tracker_team" ADD PRIMARY KEY ("id");

CREATE TABLE "octofit_tracker_user" (
    "id" bigint NOT NULL,
    "email" character varying(254) NOT NULL,
    "name" character varying(100) NOT NULL,
    "age" integer NOT NULL,
    "team" character varying(100) NOT NULL
);
ALTER TABLE "octofit_tracker_user" ADD PRIMARY KEY ("id");
ALTER TABLE "octofit_tracker_user" ADD CONSTRAINT "octofit_tracker_user_email_key" UNIQUE ("email");

CREATE TABLE "octofit_tracker_workout" (
    "id" bigint NOT NULL,
    "name" character varying(100) NOT NULL,
    "description" text NOT NULL
);
ALTER TABLE "octofit_tracker_workout" ADD PRIMARY KEY ("id");

CREATE TABLE "django_session" (
    "session_key" character varying(40) NOT NULL,
    "session_data" text NOT NULL,
    "expire_date" timestamp with time zone NOT NULL
);
ALTER TABLE "django_session" ADD PRIMARY KEY ("session_key");
INSERT INTO "django_session" ("session_key", "session_data", "expire_date") VALUES ('lok7flaqx2u0pt3pf509eqekf1wpz0je', '.eJxVjDsOwjAQBe_iGlk2_lPS5wzWeneNAyiR4qRC3B0ipYD2zcx7iQzb2vLWeckjiYvQ4vS7FcAHTzugO0y3WeI8rctY5K7Ig3Y5zMTP6-H-HTTo7VtbQIKo2SRHGl2pZBKcq6mWkiH0mjkSo1IuIidtOIAKbMB6ZT0GL94fD5Q4kw:1u6Cdq:N_ljKjEK7cKozY12SgT9m3V9wXqhO910d1vHy0aApTg', '2025-05-03 18:10:14.959588+00:00');
