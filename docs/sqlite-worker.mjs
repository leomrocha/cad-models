import {search} from './engine.mjs';
self.onmessage = async ({data}) => {
  const {request, args} = data;
  try {
    self.postMessage({request, result: await search('sqlite', ...args)});
  } catch (error) {
    self.postMessage({request, error: String(error)});
  }
};
