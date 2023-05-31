#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { SpiritsolInfraStack } from '../lib/spiritsol-infra-stack';

const app = new cdk.App();
new SpiritsolInfraStack(app, 'SpiritsolInfraStack', {
});