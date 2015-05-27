#[no_mangle]
pub extern fn rust_double(x: f64) -> f64 { 
    x * 2.0
}

#[test]
fn it_works() {
    assert!(rust_double(3.0) == 6.0)
}
