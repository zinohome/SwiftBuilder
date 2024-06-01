#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  #
#  Copyright (C) 2023 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2023
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: SwiftApp
from datetime import date, datetime
from decimal import Decimal
from fastapi_amis_admin import models, amis
from typing import Optional, List, TYPE_CHECKING

from fastapi_amis_admin.models import Field
from sqlalchemy import func
from sqlmodel import Relationship
from sqlmodelx import SQLModel

from core import i18n as _

class SwiftSQLModel(SQLModel):
    class Config:
        use_enum_values = True
        from_attributes = True
        arbitrary_types_allowed = True

class Application(SwiftSQLModel, table=True):
    __tablename__ = 'application'
    application_id: Optional[int] = models.Field(default=None,
                                                    title='ID',
                                                    primary_key=True,
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    appname: str = models.Field(default="SwiftApp",
                                                    title='应用名称',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    apptitle: str = models.Field(default="SwiftApp",
                                                    title='应用标题',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    description: str = models.Field(default="A Swift Application Builder",
                                                    title='应用描述',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    version: str = models.Field(default="v0.1",
                                                    title='应用版本',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    author: str = models.Field(default="Zinohome.com",
                                                    title='作者信息',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    host: str = models.Field(default="0.0.0.0",
                                                    title='监听地址',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    port: int = models.Field(default=8000,
                                                    title='监听端口',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    debug: bool = models.Field(default=True,
                                                    title='调试日志',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    site_icon: str = models.Field(default="https://baidu.gitee.io/amis/static/favicon_b3b0647.png",
                                                    title='页面图标',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    site_url: str = models.Field(default="None",
                                                    title='应用地址',
                                                    nullable=True,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    site_path: str = models.Field(default="/admin",
                                                    title='应用路径',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    database_url_async: str = models.Field(default="mysql+aiomysql://username:password@dbhost:dbport/dbname?charset=utf8mb4",
                                                    title='数据库连接(异步)',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    database_url: str = models.Field(default="mysql+pymysql://username:password@dbhost:dbport/dbname?charset=utf8mb4",
                                                    title='数据库连接',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    language: str = models.Field(default="zh_CN",
                                                    title='显示语言',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    amis_cdn: str = models.Field(default="https://cdn.jsdelivr.net/npm",
                                                    title='amis_cdn',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    amis_pkg: str = models.Field(default="amis@6.0.0",
                                                    title='amis_pkg',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    amis_theme: str = models.Field(default="cxd",
                                                    title='amis_theme',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    secret_key: str = models.Field(default="tr0kjyg3dls6wk2tyv816wljchqp7039hjxesccebpxd701ow4ctlfe2u0anmm60",
                                                    title='secret_key',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    allow_origins: str = models.Field(default="*",
                                                    title='allow_origins',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    create_time: datetime = models.Field(default_factory= datetime.now,
                                                    title='Create Time',
                                                    nullable=False,
                                                    index=True,
                                                    amis_form_item=amis.InputDatetime(disabled=True),
                                                    amis_table_column = "")
    update_time: Optional[datetime] = models.Field(default_factory= datetime.now,
                                                    title='Update Time',
                                                    nullable=False,
                                                    index=True,
                                                    sa_column_kwargs={"onupdate": func.now(), "server_default": func.now()},
                                                    amis_form_item=amis.InputDatetime(disabled=True),
                                                    amis_table_column = "")
