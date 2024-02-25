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
        orm_mode = True
        arbitrary_types_allowed = True

class Application(SwiftSQLModel, table=True):
    __tablename__ = 'application'
    applicaiton_id: Optional[int] = models.Field(default=None,
                                                    title='ID',
                                                    primary_key=True,
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    appname: str = models.Field(default=None,
                                                    title='应用名称',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    apptitle: str = models.Field(default=None,
                                                    title='应用标题',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    description: str = models.Field(default=None,
                                                    title='应用描述',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    version: str = models.Field(default=None,
                                                    title='应用版本',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    author: str = models.Field(default=None,
                                                    title='作者信息',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    host: str = models.Field(default=None,
                                                    title='监听地址',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    port: int = models.Field(default=None,
                                                    title='监听端口',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    debug: bool = models.Field(default=None,
                                                    title='调试日志',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    site_icon: str = models.Field(default=None,
                                                    title='页面图标',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    site_url: str = models.Field(default=None,
                                                    title='应用地址',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    site_path: str = models.Field(default=None,
                                                    title='应用路径',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    database_url_async: str = models.Field(default=None,
                                                    title='数据库连接(异步)',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    database_url: str = models.Field(default=None,
                                                    title='数据库连接',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    language: str = models.Field(default=None,
                                                    title='显示语言',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    amis_cdn: str = models.Field(default=None,
                                                    title='amis_cdn',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    amis_pkg: str = models.Field(default=None,
                                                    title='amis_pkg',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    amis_theme: str = models.Field(default=None,
                                                    title='amis_theme',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    secret_key: str = models.Field(default=None,
                                                    title='secret_key',
                                                    nullable=False,
                                                    index=False,
                                                    amis_form_item = "",
                                                    amis_table_column = "")
    allow_origins: str = models.Field(default=None,
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
