# Inspired by https://stackoverflow.com/questions/880227/what-is-the-minimum-i-have-to-do-to-create-an-rpm-file

# Install: rpm -ivh target/RPMS/x86_64/foo-cli-1.0-1.x86_64.rpm
# Remove:  rpm -ev progname

PACKAGE=foo-cli
VERSION=1.0
RELEASE=1
ARCH=x86_64
SPEC=$(PACKAGE).spec

TARGET=$(PWD)/target
RPMDIR=$(TARGET)/rpm
PKG=$(PACKAGE)-$(VERSION)
PKGGZ=$(PACKAGE)-$(VERSION).tar.gz
RPMNAME=$(PKG)-$(RELEASE).$(ARCH).rpm
TARGET_RPM=$(RPMDIR)/RPMS/$(ARCH)/$(RPMNAME)

GO=go

.PHONY: all
all: $(TARGET_RPM)

$(TARGET_RPM): $(TARGET)/$(PKGGZ)
	mkdir -p $(RPMDIR)/{BUILD,RPMS,SOURCES,SPECS,SRPMS,tmp}
	cp rpm/$(SPEC) $(RPMDIR)/SPECS
	mv $(TARGET)/$(PKGGZ) $(RPMDIR)/SOURCES
	rpmbuild	--define '%_topdir $(RPMDIR)'		\
						--define '%_package $(PACKAGE)'	\
						--define '%_version $(VERSION)'	\
						--define '%_release $(RELEASE)'	\
						--bb $(RPMDIR)/SPECS/$(SPEC)
	echo "Created $(TARGET_RPM)"

$(TARGET)/$(PKGGZ): $(TARGET)/$(PKG)
	tar cfz $(TARGET)/$(PKGGZ) -C $(TARGET) $(PKG)

# Build package file
$(TARGET)/$(PKG): $(TARGET)/foo-cli
	mkdir -p $(TARGET)/$(PKG)
	mkdir -p $(TARGET)/$(PKG)/usr/bin
	mkdir -p $(TARGET)/$(PKG)/etc/$(PACKAGE)
	install -m 755 $(TARGET)/foo-cli $(TARGET)/$(PKG)/usr/bin
	install -m 644 rpm/foo-cli.conf $(TARGET)/$(PKG)/etc/$(PACKAGE)

$(TARGET)/foo-cli: $(TARGET)
	$(GO) build -o $(TARGET)/foo-cli -i github.com/avshabanov/go-centos-build/samples/foo-cli

$(TARGET):
	mkdir $(TARGET)

# Helper targets

.PHONY: clean
clean:
	rm -rf $(TARGET)

