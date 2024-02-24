#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  #
#  Copyright (C) 2023 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2023
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: SwiftApp
from fastapi import APIRouter
from fastapi_amis_admin.crud import SqlalchemyCrud

from apps.admin.pages.contractadmin import ContractAdmin
from apps.admin.pages.contractdetailadmin import ContractdetailAdmin
from core.globals import site
from fastapi_amis_admin import amis, admin
from fastapi_amis_admin.admin import AdminApp
from construct.app import App
from utils.log import log as log

appdef = App()
class Contractadmingroup(admin.AdminApp):
    group_schema = 'Contract'
    page_schema = amis.PageSchema(label='合同管理', title='合同管理', icon='fa fa-bolt', sort=98)
    router_prefix = '/contract'

    def __init__(self, app: "AdminApp"):
        super().__init__(app)
        self.register_admin(ContractAdmin)
        self.register_admin(ContractdetailAdmin)

        
        #contractdetailAdmin_crud = ContractdetailAdmin(self.app).register_crud()
        #self.router.include_router(contractdetailAdmin_crud.router)

        '''
        contractdetail_crud = SqlalchemyCrud(model=Contractdetail, engine=site.engine,
                                             pk_name='contractdetail_id').register_crud()
        self.router.include_router(contractdetail_crud.router)
        '''
